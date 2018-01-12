import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

        dcc.Checklist(
            id = 'clts',
            values=[],
            options=[
            ],
            labelStyle={'display': 'inline-block'},
            style={"height" : "3vh", "width" : "100vw"}
        ),

        html.Div([
            dcc.Graph(
                figure={'data': [{'x': [1, 2, 3]}]},
                id='ts1',
                style={
                    "height": "100vh",
                    "width": "25vw",
                    "float": "left",
                    'display': 'inline-block'
                }
            ),
            dcc.Graph(
                figure={'data': [{'x': [1, 2, 3]}]},
                id='ts2',
                style={
                    "height": "100vh",
                    "width": "25vw",
                    "float": "left",
                    'display': 'inline-block'
                }
            ),

            dcc.Graph(
                figure={'data': [{'x': [1, 2, 3]}]},
                id='ts3',
                style={
                    "height": "100vh",
                    "width": "25vw",
                    "float": "left",
                    'display': 'inline-block'
                }
            ),
            dcc.Graph(
                figure={'data': [{'x': [1, 2, 3]}]},
                id='ts4',
                style={
                    "height": "100vh",
                    "width": "25vw",
                    "float": "left",
                    'display': 'inline-block'
                }
            ),

        ], style={"height" : "97vh", "width" : "100vw"}),

        dcc.Interval(
            id='interval-component10',
            interval=10 * 1000  # in milliseconds
        )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
