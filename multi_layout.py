import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import json

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True
app.layout = html.Div([
    html.Div([
        dcc.Input(
            value='Input {}'.format(i),
            id='input-{}'.format(i)
        )
        for i in range(10)
    ]),
    html.Div(id='container'),
])


@app.callback(
    Output('container', 'children'),
    [Input('input-{}'.format(i), 'value') for i in range(10)])
def dynamic_output(*args):
    return json.dumps(args, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)
