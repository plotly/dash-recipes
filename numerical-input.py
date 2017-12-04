import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input', type='number'),
    html.Div(id='output')
])


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('input', 'value')])
def update_output(value):
    print type(value)
    return value


if __name__ == '__main__':
    app.run_server(debug=True)
