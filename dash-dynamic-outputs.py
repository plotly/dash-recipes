import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import datetime
import json
import time


app = dash.Dash()
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    dcc.RadioItems(
        id='toggle-content',
        options=[{'label': i, 'value': i} for i in ['Hide', 'Show']],
        value='Hide'
    ),
    html.Div(id='container')
])


@app.callback(
    Output('container', 'children'),
    [Input('toggle-content', 'value')])
def display_output(value):
    if value == 'Hide':
        return ''
    return html.Div([
        html.Div([
            dcc.Input(value='Input {}'.format(i), id='input-{}'.format(i))
            for i in range(10)
        ]),
        html.Div(id='dynamic-output')
    ])


@app.callback(
    Output('dynamic-output', 'children'),
    [Input('input-{}'.format(i), 'value') for i in range(10)])
def dynamic_output(*args):
    print(args)
    time.sleep(2)
    return [html.Strong(datetime.datetime.now()), json.dumps(args, indent=2)]


if __name__ == '__main__':
    app.run_server(debug=True)
