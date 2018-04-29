# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import plotly.graph_objs as go

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True
server = app.server

x, y, z = np.random.multivariate_normal(
    np.array([0, 0, 0]), np.eye(3), 2).transpose()

app.layout = html.Div([
        dcc.Slider(
            id='slider',
            min=0,
            max=20,
            value=0,
            step=None,
            marks={str(n): str(n) for n in range(20)},
        ),
        dcc.Graph(
            id='scatter_3d_0',
            figure={
                'data': [
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ],
            }
        ),
        dcc.Graph(
            id='scatter_3d_1',
            figure={
                'data': [
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ],
            }
        ),
        dcc.Graph(
            id='scatter_3d_1',
            figure={
                'data': [
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ],
            }
        ),
        dcc.Graph(
            id='scatter_3d_2',
            figure={
                'data': [
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ],
            }
        ),
        dcc.Graph(
            id='scatter_3d_3',
            figure={
                'data': [
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ],
            }
        )
])



@app.callback(
    Output('scatter_3d_1', 'figure'),
    [ Input('slider', 'value')],
    [State('scatter_3d_1', 'figure')])

def display_scatter_3d_1(value,figure):
    x, y, z = np.random.multivariate_normal(
     np.array([0, 0, 0]), np.eye(3), 2).transpose()
    figure['data']=[
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ]
    return figure


@app.callback(
    Output('scatter_3d_2', 'figure'),
    [ Input('slider', 'value')],
    [State('scatter_3d_2', 'figure')])

def display_scatter_3d_2(value,figure):
    x, y, z = np.random.multivariate_normal(
     np.array([0, 0, 0]), np.eye(3), 2).transpose()
    figure['data']=[
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ]
    return figure


@app.callback(
    Output('scatter_3d_3', 'figure'),
    [ Input('slider', 'value')],
    [State('scatter_3d_3', 'figure')])

def display_scatter_3d_3(value,figure):
    x, y, z = np.random.multivariate_normal(
     np.array([0, 0, 0]), np.eye(3), 2).transpose()
    figure['data']=[
                    go.Scatter3d(
                        x=x,
                        y=y,
                        z=z,
                        mode='markers',
                    )
                ]
    return figure



if __name__ == '__main__':
    app.run_server(debug=True)
