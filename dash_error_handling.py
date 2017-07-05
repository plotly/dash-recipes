import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-input'),
    html.Div(id='my-output')
])
    

@app.callback(dash.dependencies.Output('my-output', 'children'), [dash.dependencies.Input('my-input', 'value')])
def update_output(input_value):
    import ipdb; ipdb.set_trace()
    raise Exception('error!')

if __name__ == '__main__':
    app.run_server(debug=True)

