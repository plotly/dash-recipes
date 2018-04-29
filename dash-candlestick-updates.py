import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc


app = dash.Dash(__name__)
app.layout = html.Div([
    html.Button(
        id='button',
        children='Update Candlestick',
        n_clicks=0
    ),
    dcc.Graph(id='graph')
])

@app.callback(Output('graph', 'figure'), [Input('button', 'n_clicks')])
def update_graph(n_clicks):
    return {
        'data': [{
            'open': [1] * 5,
            'high': [3] * 5,
            'low': [0] * 5,
            'close': [2] * 5,
            'x': [n_clicks] * 5,
            'type': 'candlestick'
        }],
        'layout': {
            'title': 'x is {}'.format(n_clicks)
        }
    }

if __name__ == '__main__':
    app.run_server(debug=True)
