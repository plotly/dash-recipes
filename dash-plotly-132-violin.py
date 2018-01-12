import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')

app = dash.Dash()

app.layout = html.Div(className='container', children=[
    html.H1('Plotly.js Violin Plots in Dash'),
    html.Hr(),
    html.Div(className='two columns', children=[
        dcc.RadioItems(
            id='items',
            options=[
                {'label': 'Sepal Length', 'value': 'SepalLength'},
                {'label': 'Sepal Width', 'value': 'SepalWidth'},
                {'label': 'Petal Length', 'value': 'PetalLength'},
                {'label': 'Petal Width', 'value': 'PetalWidth'}
            ],
            value='SepalLength',
            style={'display': 'block'}
        ),
        html.Hr(),
        dcc.RadioItems(
            id='points',
            options=[
                {'label': 'Display All Points', 'value': 'all'},
                {'label': 'Hide Points', 'value': False},
                {'label': 'Display Outliers', 'value': 'outliers'},
                {'label': 'Display Suspected Outliers', 'value': 'suspectedoutliers'},
            ],
            value='all',
            style={'display': 'block'}
        ),
        html.Hr(),
        html.Label('Jitter'),
        dcc.Slider(
            id='jitter',
            min=0,
            max=1,
            step=0.1,
            value=0.7,
            updatemode='drag'
        )
    ]),
    html.Div(dcc.Graph(id='graph'), className='ten columns')
])

@app.callback(
    Output('graph', 'figure'), [
    Input('items', 'value'),
    Input('points', 'value'),
    Input('jitter', 'value')])
def update_graph(value, points, jitter):
    return {
        'data': [
            {
                'type': 'violin',
                'x': df['Name'],
                'y': df[value],
                'text': ['Sample {}'.format(i) for i in range(len(df))],
                'points': points,
                'jitter': jitter
            }
        ],
        'layout': {
            'margin': {'l': 30, 'r': 10, 'b': 30, 't': 0}
        }
    }

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/dZVMbK.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
