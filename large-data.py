import dash
import dash_core_components as dcc
import dash_html_components as html

import json
import numpy as np

app = dash.Dash()

N = 100*1000*1000

app.layout = html.Div([
    html.Div(
        dcc.Graph(
            id='graph',
            figure={
                'data': [{
                    'x': np.random.randn(N, 1),
                    'Y': np.random.randn(N, 1)
                }]
            }
        ), style={
            'display': 'none'
        }
    ),
    dcc.Input(id='input', value=''),
    html.Div(id='output', style={'display': 'none'})
])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input', 'value')])
def update_output(value):
    return json.dumps(list(range(N)))

if __name__ == '__main__':
    app.run_server(debug=True)
