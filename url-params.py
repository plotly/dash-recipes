import dash
import dash_core_components as dcc
import dash_html_components as html

import flask

app = dash.Dash()
server = app.server

app.layout = html.Div([
    dcc.Location(id='path'),
    html.Div(id='output')
])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('path', 'pathname')])
def update_output(value):
    print('Request', value, flask.request.args)

    return value


if __name__ == '__main__':
    app.run_server()
