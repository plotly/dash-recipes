import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc


app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True
app.scripts.config.serve_locally = True

layout = html.Div([
    html.H3('App 1'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),
    dcc.Link('Go to App 2', href='/apps/app2'),
    html.Div(id='searchRes1'),
])

@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


app.layout = html.Div([dcc.Location(id='url', refresh=False),
                       html.Div(id='searchRes2'),
                       html.H1('Test'),
                       html.Div(id='page-content')])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print('display_page')
    return layout

@app.callback(Output('searchRes1', 'children'),
              [Input('url', 'search')])
def display_value(search):
    print('searchRes1')
    if search is None or search is '':
        return 'no Search'
    return 'searchRes1: {}'.format(search)

@app.callback(Output('searchRes2', 'children'),
              [Input('url', 'search')])
def display_value(search):
    print('searchRes2')
    if search is None:
        return 'no search'
    return 'searchRes2: {}'.format(search)

if __name__ == '__main__':
    app.run_server(debug = True) #host = '0.0.0.0', port=8051)
