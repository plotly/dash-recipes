import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

app = dash.Dash()

app.layout = html.Div([
    html.Button(id='button', n_clicks=0, children='Load'),
    dcc.Graph(id='graph')
])


x = np.random.randn(1000 * 1000)
y = np.random.randn(1000 * 1000)


@app.callback(Output('graph', 'figure'), [Input('button', 'n_clicks')])
def update_graph(n_clicks):
    if n_clicks > 0:
        return {
            'data': [{
                'x': x,
                'y': y,
                'type': 'scattergl'
            }]
        }


if __name__ == '__main__':
    app.run_server(debug=True)
