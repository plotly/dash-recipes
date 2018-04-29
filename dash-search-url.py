import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc


app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True
app.scripts.config.serve_locally = True


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Dropdown(
        id='dropdown',
        value='a',
        options=[{'label': i, 'value': i} for i in ['a', 'b']]
    ),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('dropdown', 'value')])
def display_page(pathname):
    return [html.Div([
        html.Div('Page 1'),
        html.Div(id='page-1')
    ])]

@app.callback(Output('page-1', 'children'),
              [Input('dropdown', 'value')])
def display_value(search):
    print('page-1')
    if search is None or search is '':
        return 'no Search'
    return 'page-1: {}'.format(search)

if __name__ == '__main__':
    app.run_server(debug = True)
