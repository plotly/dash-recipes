import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='grandparent',
        options=[{'label': i, 'value': i} for i in range(5)],
        value=0
    ),
    html.Div(id='parent-a'),
    html.Div(id='parent-b'),
    html.Div(id='child')
])


@app.callback(Output('parent-a', 'children'), [Input('grandparent', 'value')])
def update_parent_a(value):
    print('update_parent_a')
    return 'Parent A with {}'.format(value)


@app.callback(Output('parent-b', 'children'), [Input('grandparent', 'value')])
def update_parent_b(value):
    print('update_parent_b')
    return 'Parent B with {}'.format(value)


@app.callback(Output('child', 'children'),
              [Input('parent-a', 'children'),
               Input('parent-b', 'children')])
def update_child(parent_a, parent_b):
    print('update_child')
    return 'Child with "{}" and "{}"'.format(parent_a, parent_b)


if __name__ == '__main__':
    app.run_server(debug=True)
