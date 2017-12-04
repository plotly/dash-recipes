import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='my-graph',
        figure={
            'data': [{
                'x': [1, 2, 3],
                'y': [3, 1, 2]
            }],
            'layout': {
                'yaxis': {
                    'scaleanchor': 'x'
                },
                'height': 700
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
