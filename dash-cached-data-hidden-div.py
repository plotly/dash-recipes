import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6],
    'y': [3, 1, 2, 3, 5, 6],
    'z': ['A', 'A', 'B', 'B', 'C', 'C']
})

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['A', 'B', 'C']],
        value='A'
    ),

    dcc.Graph(
        id='graph'
    ),

    html.Div(id='cache', style={'display': 'none'})
])


@app.callback(Output('cache', 'children'), [Input('dropdown', 'value')])
def update_cache(value):
    filtered_df = df[df['z'] == value]
    return filtered_df.to_json()


@app.callback(Output('graph', 'figure'), [Input('cache', 'children')])
def update_graph(cached_data):
    filtered_df = pd.read_json(cached_data)
    return {
        'data': [{
            'x': filtered_df['x'],
            'y': filtered_df['y'],
            'type': 'bar'
        }]
    }


if __name__ == '__main__':
    app.run_server(debug=True)
