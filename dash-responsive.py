import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Div(
            dcc.Graph(id='graph-1', figure={
                'data': [{
                    'x': [1, 2, 3],
                    'y': [4, 1, 3]
                }]
            }),
            className="six columns"
        ),
        html.Div(
            dcc.Graph(id='graph-2', figure={
                'data': [{
                    'x': [1, 2, 3],
                    'y': [4, 1, 3]
                }]
            }),
            className="six columns"
        )
    ], className="row")
])

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
