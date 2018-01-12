import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import json
import pandas as pd
import numpy as np
import plotly

app = dash.Dash()

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
)
df = df[df['year'] == 2007]

axis = {
    'zeroline': False,
    'ticks': '',
    'showgrid': False
}

app.layout = html.Div([
    html.H2('Multiple Selections'),

    html.Div(className='row', children=[
        html.Div(
            className='six columns',
            children=dcc.Graph(
                id='scatter',
                figure={
                    'data': [{
                        'x': df['gdpPercap'],
                        'y': df['lifeExp'],
                        'text': df['country'],
                        'marker': {
                            'size': df['pop'],
                            'sizemode': 'area',
                            'sizeref': 2.*df['pop'].max() / (50. ** 2),
                            'sizemin': 4
                        },
                        'type': 'scatter',
                        'mode': 'markers'
                    }],
                    'layout': {
                        'margin': {'l': 20, 'r': 0, 'b': 40, 't': 10},
                        'xaxis': dict(type='log', **axis),
                        'yaxis': axis,
                        'height': 800
                    }
                }
            )
        ),
        html.Div(
            className='six columns',
            children=[
                dcc.Graph(id='gdp-histogram'),
                dcc.Graph(id='lifeExp-histogram')
            ]
        )
    ])
], className="container")

def histogram(selected_data, column):
    if selected_data:
        indices = [point['pointIndex'] for point in selected_data['points']]
        dff = df.iloc[indices, :]
    else:
        dff = df
    fig = {
        'data': [{
            'x': dff[column],
            'type': 'violin'
        }],
        'layout': {
            'margin': {'l': 0, 'r': 0, 'b': 40, 't': 5},
            'xaxis': axis,
            'yaxis': axis,
            'height': 400
        }
    }

    return fig

@app.callback(
    Output('gdp-histogram', 'figure'),
    [Input('scatter', 'selectedData')])
def update_gdp(selected_data):
    return histogram(selected_data, 'gdpPercap')

@app.callback(
    Output('lifeExp-histogram', 'figure'),
    [Input('scatter', 'selectedData')])
def update_life_exp(selected_data):
    return histogram(selected_data, 'lifeExp')


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
