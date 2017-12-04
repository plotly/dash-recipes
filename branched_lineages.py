import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import time

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    dcc.Input(id='grandparent', value='input 1'),
    dcc.Input(id='parent-a'),
    dcc.Input(id='parent-b'),
    dcc.Input(id='parent-c'),
    html.Div(id='child-a'),
    html.Div(id='child-b')
])

app.scripts.config.serve_locally = True


@app.callback(Output('parent-a', 'value'),
              [Input('grandparent', 'value')])
def update_parenta(value):
    print('parenta')
    time.sleep(2)
    return 'a: {}'.format(value)


@app.callback(Output('parent-b', 'value'),
              [Input('grandparent', 'value')])
def update_parentb(value):
    print('parentb')
    time.sleep(6)
    return 'b: {}'.format(value)


@app.callback(Output('parent-c', 'value'),
              [Input('grandparent', 'value')])
def update_parentb(value):
    print('parentc')
    time.sleep(9)
    return 'c: {}'.format(value)


@app.callback(Output('child-a', 'children'),
              [Input('parent-a', 'value'),
               Input('parent-b', 'value'),
               Input('parent-c', 'value')])
def update_childa(parenta_value, parentb_value, parentc_value):
    print('childa: {}, {}, {}'.format(parenta_value, parentb_value, parentc_value))
    raise Exception
    return 'childa: {} + {} + {}'.format(parenta_value, parentb_value, parentc_value)


@app.callback(Output('child-b', 'children'),
              [Input('parent-a', 'value'),
               Input('parent-b', 'value'),
               Input('grandparent', 'value')])
def update_childb(parenta_value, parentb_value, grandparent_value):
    print('childb: {}, {}, {}'.format(
        parenta_value,
        parentb_value,
        grandparent_value
    ))
    return 'childb: {} + {} + {}'.format(
        parenta_value,
        parentb_value,
        grandparent_value
    )


if __name__ == '__main__':
    app.run_server(debug=True, processes=8)
