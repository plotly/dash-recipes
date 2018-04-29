import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import json

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='graph',
        figure={
            'data': [{
                'x': [1, 2, 3],
                'y': [3, 1, 2]
            }]
        }
    ),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['a', 'b', 'c']]
    ),
    html.Pre(id='output')
])

@app.callback(Output('output', 'children'), [
    Input('graph', 'clickData'),
    Input('dropdown', 'value')])
def update_output(*args):
    return json.dumps(args, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)
