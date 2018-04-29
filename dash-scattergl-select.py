import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
import pandas as pd

app = dash.Dash()

df = pd.DataFrame({
    'Column {}'.format(i): np.random.rand(50) + i*10
    for i in range(6)})

app.layout = html.Div([
    html.Div(
        dcc.Graph(
            id='g1',
            selectedData={'points': [], 'range': None}
        ), className="four columns"
    ),
    html.Div(
        dcc.Graph(
            id='g2',
            selectedData={'points': [], 'range': None}
        ), className="four columns"),
    html.Div(
        dcc.Graph(
            id='g3',
            selectedData={'points': [], 'range': None}
        ), className="four columns")
], className="row")


def highlight(x, y):
    def callback(*selectedDatas):
        index = df.index
        for i, hover_data in enumerate(selectedDatas):
            selected_index = [
                p['customdata'] for p in selectedDatas[i]['points']
                # the first trace that includes all the data
                if p['curveNumber'] == 0
            ]
            if len(selected_index) > 0:
                index = np.intersect1d(index, selected_index)

        dff = df.iloc[index, :]


        figure = {
            'data': [
                dict({
                    'x': df[x], 'y': df[y], 'text': df.index,
                    'customdata': df.index,
                    'mode':'markers',
                    'type': 'scattergl', 'opacity': 0.1
                }),
                dict({
                    'x': dff[x], 'y': dff[y], 'text': dff.index,
                    'mode':'markers',
                    'type': 'scattergl', 'textposition': 'top',
                }),
            ],
            'layout': {
                'margin': {'l': 20, 'r': 0, 'b': 20, 't': 5},
                'dragmode': 'select',
                'hovermode': 'closest',
                'showlegend': False
            }
        }


        return figure

    return callback


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# app.callback is a decorator which means that it takes a function
# as its argument.
# highlight is a function "generator": it's a function that returns function
app.callback(
    Output('g1', 'figure'),
    [Input('g1', 'selectedData'),
     Input('g2', 'selectedData'),
     Input('g3', 'selectedData')]
)(highlight('Column 0', 'Column 1'))

app.callback(
    Output('g2', 'figure'),
    [Input('g2', 'selectedData'),
     Input('g1', 'selectedData'),
     Input('g3', 'selectedData')]
)(highlight('Column 2', 'Column 3'))

app.callback(
    Output('g3', 'figure'),
    [Input('g3', 'selectedData'),
     Input('g1', 'selectedData'),
     Input('g2', 'selectedData')]
)(highlight('Column 4', 'Column 5'))

if __name__ == '__main__':
    app.run_server(debug=True)
