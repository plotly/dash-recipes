import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import json

app = dash.Dash()

options = {
    'America': ['NYC', 'Cincinatti'],
    'Canada': ['Montreal', 'Toronto'],
}

app.layout = html.Div([
    dcc.Dropdown(
        id='d1',
        options=[{'label': i, 'value': i} for i in options.keys()],
        value='Canada'
    ),
    dcc.Dropdown(
        id='d2'
    ),
    html.Div('{}', id='history', style={'display': 'none'})
])


@app.callback(Output('d2', 'options'), [Input('d1', 'value')])
def update_options(value):
    return [{'label': i, 'value': i} for i in options[value]]


@app.callback(Output('d2', 'value'),
              [Input('d2', 'options')],
              [State('d1', 'value'), State('history', 'children')])
def update_value(options, d1value, jhistory):
    history = json.loads(jhistory)
    if d1value in history:
        return history[d1value]
    return options[0]['value']


@app.callback(Output('history', 'children'),
              [Input('d1', 'value'), Input('d2', 'value')],
              [State('history', 'children')])
def update_history(d1value, d2value, jhistory):
    history = json.loads(jhistory)
    history[d1value] = d2value
    return json.dumps(history)


if __name__ == '__main__':
    app.run_server(debug=True)
