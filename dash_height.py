import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='graph-1',
        figure={
            'data': [{
                'y': [1, 4, 3]
            }],
            'layout': {
                'height': 800
            }
        }
    ),
    html.Hr(),
    dcc.Graph(
        id='graph-2',
        style={
            'height': 800
        },
        figure={
            'data': [{
                'y': [1, 5, 2]
            }]
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
