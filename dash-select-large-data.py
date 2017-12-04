import numpy as np

# plotting imports
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

app = dash.Dash()

N = 1000

app.layout = html.Div([
    html.Div(id='output'),
    dcc.Graph(
        id='plot',
        figure={
            'data': [{
                'x': np.random.randn(N),
                'y': np.random.randn(N),
                'mode': 'markers'
            }]
        },
        selectedData={
            'points': []
        }
    )
], style={'width': '100%'})


@app.callback(
    Output('output', 'children'),
    [Input('plot', 'selectedData')])
def display_points(selectedData):
    return 'You have selected {} points'.format(
        len(selectedData['points']))


if __name__ == '__main__':
    app.run_server(debug=True)
