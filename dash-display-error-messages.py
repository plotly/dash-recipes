import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import flask
import os

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input', value=''),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input('input', 'value')])
def output(value):
    flask.session['error-message'] = 'test'
    if value == 'error':
        1/0
    else:
        return value

app.scripts.append_script({
    'external_url': '/static/dash-error-message-display.js'
})

@app.server.route('/static/<filename>.js')
def serve_script(filename):
    print(('serving {}'.format(filename)))
    if filename not in ['dash-error-message-display']:
        raise Exception('"{}" is excluded from the allowed static files'.format(filename))
    return flask.send_from_directory(os.getcwd(), '{}.js'.format(filename))


if __name__ == '__main__':
    app.run_server(debug=True)
