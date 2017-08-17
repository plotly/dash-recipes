import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value'),
    html.Div(id='output')
])

@app.callback(
	dash.dependencies.Output('output', 'children'), 
	[dash.dependencies.Input('input', 'value')])
def update_output(value):
    print(value)
    return value

server = app.server
server.secret_key = 'secret'
