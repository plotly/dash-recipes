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

        color = 'rgb(125, 58, 235)'

        trace_template = {
            'marker': {
                'color': color,
                'size': 12,
                'line': {'width': 0.5, 'color': 'white'}
            }
        }
        figure = {
            'data': [
                dict({
                    'x': df[x], 'y': df[y], 'text': df.index,
                    'customdata': df.index,
                    'mode': 'markers', 'opacity': 0.1
                }, **trace_template),
                dict({
                    'x': dff[x], 'y': dff[y], 'text': dff.index,
                    'mode': 'markers+text', 'textposition': 'top',
                }, **trace_template),
            ],
            'layout': {
                'margin': {'l': 20, 'r': 0, 'b': 20, 't': 5},
                'dragmode': 'select',
                'hovermode': 'closest',
                'showlegend': False
            }
        }

        shape = {
            'type': 'rect',
            'line': {
                'width': 1,
                'dash': 'dot',
                'color': 'darkgrey'
            }
        }
        if selectedDatas[0]['range']:
            figure['layout']['shapes'] = [dict({
                'x0': selectedDatas[0]['range']['x'][0],
                'x1': selectedDatas[0]['range']['x'][1],
                'y0': selectedDatas[0]['range']['y'][0],
                'y1': selectedDatas[0]['range']['y'][1]
            }, **shape)]
        else:
            figure['layout']['shapes'] = [dict({
                'type': 'rect',
                'x0': np.min(df[x]),
                'x1': np.max(df[x]),
                'y0': np.min(df[y]),
                'y1': np.max(df[y])
            }, **shape)]

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
