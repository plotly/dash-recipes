import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        value=['a'],
        options=[{'label': i, 'value': i} for i in ['a', 'b', 'c', 'd']],
        multi=True,
        id='dropdown'
    ),
    html.H3(id='output')
])

@app.callback(Output('output', 'children'), [Input('dropdown', 'value')])
def display_output(value):
    return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)
