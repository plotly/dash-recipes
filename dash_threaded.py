import dash
import dash_core_components as dcc
import dash_html_components as html

import time

app = dash.Dash()
server = app.server

app.layout = html.Div([
    dcc.Input(id='input'),
    html.Div(id='output')
])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input', 'value')])
def update_output(value):
    print('Request')
    time.sleep(20)
    return value


if __name__ == '__main__':
    app.run_server(threaded=True)
