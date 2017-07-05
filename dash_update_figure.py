import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import numpy as np

x_data = np.linspace(0,500,500)
y_data = np.random.rand(500)
height = max(y_data)

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='basic_graph')])

@app.callback(dash.dependencies.Output('basic_graph', 'figure'),
              [dash.dependencies.Input('basic_graph', 'hoverData')])
def update_graph(hoverData):
    if not hoverData:
        x_value=x_data[250]
        opacity = 0
    else:
        x_value = hoverData['points'][0]['x']
        opacity = 0.8
    data = [go.Scatter(
                x=x_data,
                y=y_data,
                line={'color': '#235ebc'},
                opacity=0.8,
                name="Graph"
            ),
            go.Scatter(
                x=[x_value, x_value],
                y=[0, height],
                line={'color': '#a39999'},
                opacity=opacity,
                name='Moving Line')
            ]
    layout = go.Layout(
                xaxis={'type': 'linear', 'title': "Timestep"},
                yaxis={'type': 'linear', 'title': "Value"},
                margin={'l': 60, 'b': 40, 'r': 10, 't': 10},
                hovermode="False"
                )
    
    return {'data': data, 'layout': layout}

if __name__ == '__main__':
    app.run_server()
