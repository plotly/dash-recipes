import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.Div(id='session-id', children='id'),
    dcc.Dropdown(id='dropdown-1'),
    dcc.Dropdown(id='dropdown-2'),
])

options = [{'value': 'a', 'label': 'a'}]

@app.callback(
    Output(component_id = 'dropdown-2', component_property = 'options'),
    [Input(component_id = 'dropdown-2', component_property = 'value'),
     Input('session-id', 'children')])
def dropdown_1(value, session_id):
    print('dropdown-1')
    return options

@app.callback(
    Output(component_id = 'dropdown-1', component_property = 'options'),
    [Input(component_id = 'dropdown-1', component_property = 'value'),
     Input('session-id', 'children')])
def dropdown_2(value, session_id):
    print('dropdown-2')
    return options


if __name__ == '__main__':
    app.run_server(debug=True)
