import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

dropdown_options = [
    {'label':'test_label1', 'value':1},
    {'label':'test_label2', 'value':2},
]

app = dash.Dash()

app.layout = html.Div([
    html.H1(children='dropdown_test'),
    dcc.Dropdown(
        id='dropdown',
        options=dropdown_options,
        value='1'
    ),
    html.Div(id='target')
])

@app.callback(Output('target', 'children'), [Input('dropdown', 'value')])
def callback2(value):
    print(type(value))
    return value

if __name__ == '__main__':
    app.run_server(debug=True)
