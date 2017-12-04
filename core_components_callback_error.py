import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import datetime

print(dcc.__version__)

def serve_layout():
    return html.Div([
        html.Div(id='state-container', style={'display': 'none'}),
        html.Div(id='output'),
        dcc.Dropdown(id='dropdown', options=[{'label': i, 'value': i} for i in ['A', 'B']])
    ])

app = dash.Dash()

app.layout = serve_layout

app.config.supress_callback_exceptions = True

@app.callback(
    Output('state-container', 'children'),
    [Input('dropdown', 'value')])
def update_state(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('output', 'children'),
    [Input('state-container', 'children')])
def update_output(value):
    return value


if __name__ == '__main__':
    app.run_server()
