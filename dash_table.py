import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import json
import pandas as pd
import numpy as np
import plotly

app = dash.Dash()

app.scripts.config.serve_locally=True

DF_WALMART = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')

DF_GAPMINDER = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
)
DF_GAPMINDER = DF_GAPMINDER[DF_GAPMINDER['year'] == 2007]

DF_SIMPLE = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D', 'E', 'F'],
    'y': [4, 3, 1, 2, 3, 6],
    'z': ['a', 'b', 'c', 'a', 'b', 'c']
})

app.layout = html.Div([
    html.H4('Gapminder DataTable'),
    dt.DataTable(
        rows=DF_GAPMINDER.to_dict('records'),
        filterable=False,
        sortable=True,
        id='datatable-gapminder'
    ),
    dcc.Graph(
        id='graph-gapminder'
    ),

    html.H4('Simple DataTable'),
    dt.DataTable(
        rows=DF_SIMPLE.to_dict('records'),
        filterable=False,
        sortable=True,
        id='datatable'
    ),
    dcc.Graph(
        id='graph'
    ),
], className="container")

@app.callback(
    Output('graph', 'figure'),
    [Input('datatable', 'rows')])
def update_figure(rows):
    dff = pd.DataFrame(rows)
    return {
        'data': [{
            'x': dff['x'],
            'y': dff['y'],
            'text': dff['z'],
            'type': 'bar'
        }]
    }

@app.callback(
    Output('graph-gapminder', 'figure'),
    [Input('datatable-gapminder', 'rows')])
def update_figure(rows):
    dff = pd.DataFrame(rows)
    fig = plotly.tools.make_subplots(
        rows=3, cols=1,
        subplot_titles=('Life Expectancy', 'GDP Per Capita', 'Population',),
        shared_xaxes=True)
    marker = {'color': '#0074D9'}
    fig.append_trace({
        'x': dff['country'],
        'y': dff['lifeExp'],
        'type': 'bar',
        'marker': marker
    }, 1, 1)
    fig.append_trace({
        'x': dff['country'],
        'y': dff['gdpPercap'],
        'type': 'bar',
        'marker': marker
    }, 2, 1)
    fig.append_trace({
        'x': dff['country'],
        'y': dff['pop'],
        'type': 'bar',
        'marker': marker
    }, 3, 1)
    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 800
    fig['layout']['margin'] = {
        'l': 20,
        'r': 20,
        't': 60,
        'b': 200
    }
    return fig

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
