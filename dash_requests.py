import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='d',
        options=[{'label': i, 'value': i} for i in ['a', 'b', 'c']],
        value='a'
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('d', 'value')])
def update_outout(value):
    print((flask.request.cookies))
    return value

if __name__ == '__main__':
    app.run_server(debug=True)
