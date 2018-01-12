import dash
import dash_core_components as dcc

app = dash.Dash()

app.layout = dcc.Graph(id='selected', figure={
    'data': [{
        "x": [1, 2, 3, 4],
        "y": [3, 1, 2, 5],
        "mode": "markers",
        "marker": {
            "size": 18
        },

        "selectedpoints": [0, 2],

        "selected": {
            "marker": {
                "color": "#0074D9"
            }
        },
        "unselected": {
            "marker": {
                "color": "#7FDBFF"
            }
        }
    }]
})

if __name__ == '__main__':
    app.run_server(debug=True)
