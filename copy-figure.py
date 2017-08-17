import dash
import dash_core_components as dcc
import dash_html_components as html
import copy

app = dash.Dash()

FIGURE = {
    'data': [
        {'x': [1, 2, 3], 'y': [4, 2, 1], 'type': 'bar'}
    ]
}

app.layout = html.Div([
    dcc.Dropdown(
        id='color',
        options=[
            {'label': i, 'value': i} for i in ['blue', 'red', 'black']
        ],
        value='blue'
    ),
    dcc.Graph(id='graph', figure=FIGURE)
])


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('color', 'value')])
def update_graph(color):
    copied_figure = copy.deepcopy(FIGURE)
    copied_figure['data'][0]['marker'] = {'color': color}
    return copied_figure


if __name__ == '__main__':
    app.run_server(debug=True)
