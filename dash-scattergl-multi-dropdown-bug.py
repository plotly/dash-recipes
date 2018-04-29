import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

df = pd.DataFrame({
    'x': range(50000) + range(50000),
    'y': range(100000),
    'text': range(100000),
    'filter': (['a'] * 50000) + (['b'] * 50000)
})

app.layout = html.Div([
    dcc.Dropdown(
        multi=True,
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['a', 'b']],
        value=['a']
    ),
    dcc.Graph(
        id='graph',
        animate=True
    )
])

@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value')])
def update_graph(value):
    dff = df[df['filter'].str.contains('|'.join(value))]
    return {
        'data': [{
            'x': dff['x'],
            'y': dff['y'],
            'text': dff['text'],
            'mode': 'markers',
            'type': 'scattergl'
        }]
    }

if __name__ == '__main__':
    app.run_server(debug=True)
