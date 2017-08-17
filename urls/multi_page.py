# pip install dash_core_components==0.5.3rc1

import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    # This "header" will persist across pages
    html.H2('Multi Page Dash App'),

    # Each "page" will modify this element
    html.Div(id='content-container'),

    # This Location component represents the URL bar
    dcc.Location(id='url', refresh=False)
], className="container")

@app.callback(
    Output('content-container', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/':
        return html.Div([
            html.Div('You are on the index page.'),

            # the dcc.Link component updates the `Location` pathname
            # without refreshing the page
            dcc.Link(html.A('Go to page 2 without refreshing!'), href="/page-2", style={'color': 'blue', 'text-decoration': 'none'}),
            html.Hr(),
            html.A('Go to page 2 but refresh the page', href="/page-2")
        ])
    elif pathname == '/page-2':
        return html.Div([
            html.H4('Welcome to Page 2'),
            dcc.Link(html.A('Go back home'), href="/"),
        ])
    else:
        return html.Div('I guess this is like a 404 - no content available')

# app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True)
