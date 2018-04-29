import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id='graph', figure={
        'data': [{
            'x': [1, 2, 3],
            'y': [1, 1, 1],
            'text': ['a', None, 'b'],
            'hovertext': ['x', 'y', 'z'],
            'mode': 'markers+text',
            'textposition': 'top'
        }]
    })
])

if __name__ == '__main__':
    app.run_server(debug=True)
