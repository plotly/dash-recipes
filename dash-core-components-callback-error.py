# https://community.plot.ly/t/dash-core-components-callback-error/5655/3
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import datetime

print(dcc.__version__)

def serve_layout():
    return html.Div([
        html.Div(id='state-container'),
        dcc.Dropdown(id='dropdown', options=[{'label': i, 'value': i} for i in ['A', 'B']]),
        dcc.Dropdown(id='output', options=[{}])
    ])

app = dash.Dash()

app.layout = serve_layout()

app.config.supress_callback_exceptions = True

@app.callback(
    Output('state-container', 'children'),
    [Input('dropdown', 'value')])
def update_state(value):
    print('Calling update_state: {}'.format(repr(value)))
    if value:
        return 'You have selected "{}"'.format(value)


@app.callback(
    Output('output', 'options'),
    [Input('state-container', 'children')])
def update_output(value):
    print('Calling update_output: {}'.format(repr(value)))
    if value:
        return [{'label': i, 'value': i} for i in ['C', 'D']]
    else:
        return [{}]

if __name__ == '__main__':
    app.run_server(debug=True)
