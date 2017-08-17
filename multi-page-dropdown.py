import dash
from dash.dependencies import Input, State, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'y': [3, 2, 4, 1, 4, 5, 4, 3, 1],
    'group-1': ['/', '/exhibit-b', '/exhibit-c', '/', '/exhibit-b', '/exhibit-c', '/', '/exhibit-b', '/exhibit-c'],
    'group-2': ['LA', 'LA', 'LA', 'London', 'London', 'London', 'Montreal', 'Montreal', 'Montreal'],
})

app = dash.Dash()
app.scripts.config.serve_locally=True

app.config.supress_callback_exceptions = True

app.layout = html.Div([
    # This "header" will persist across pages
    html.H2('Multi Page Dash App'),


    # Each "page" will modify this element
    html.Div(id='content-container-part-1'),


    dcc.Dropdown(
        id='graph-control',
        options=[{'label': i, 'value': i} for i in df['group-2'].unique()],
        value='LA'
    ),

    # Each "page" will modify this element
    html.Div(id='content-container-part-2'),

    # This Location component represents the URL bar
    dcc.Location(id='url', refresh=False)
], className="container")

link_mapping = {
    '/': 'Exhibit A',
    '/exhibit-b': 'Exhibit B',
    '/exhibit-c': 'Exhibit C',
}

styles = {
    'link': {'padding': '20'}
}

@app.callback(
    Output('content-container-part-1', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    return html.Div([
        html.Div([
            html.Span(
                dcc.Link(link_mapping['/'], href="/") if pathname != '/' else 'Exhibit A',
                style=styles['link']
            ),

            html.Span(
                dcc.Link(link_mapping['/exhibit-b'], href="/exhibit-b") if pathname != '/exhibit-b' else 'Exhibit B',
                style=styles['link']
            ),

            html.Span(
                dcc.Link(link_mapping['/exhibit-c'], href="/exhibit-c") if pathname != '/exhibit-c' else 'Exhibit C',
                style=styles['link']
            )

        ]),

        dcc.Markdown('### {}'.format(link_mapping[pathname])),
    ])


@app.callback(
    Output('content-container-part-2', 'children'),
    [Input('url', 'pathname')])
def display_page(*args):
    return html.Div([
        dcc.Graph(
            id='graph',
        )
    ])


@app.callback(
    Output('graph', 'figure'),
    [Input('graph-control', 'value'),
     Input('url', 'pathname')])
def update_graph(value, pathname):
    dff = df[(df['group-1'] == pathname) & (df['group-2'] == value)]
    return {
        'data': [{
            'x': dff.x,
            'y': dff.y,
            'type': 'bar'
        }],
        'layout': {
            'title': '{} in {}'.format(value, link_mapping[pathname])
        }
    }

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
