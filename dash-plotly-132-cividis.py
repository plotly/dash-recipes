import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')

app = dash.Dash()

colors = {
    'background': 'rgb(0, 32, 76)',
    'text': '#B3C8E5'
}

options = [
    {'label': 'Sepal Length', 'value': 'SepalLength'},
    {'label': 'Sepal Width', 'value': 'SepalWidth'},
    {'label': 'Petal Length', 'value': 'PetalLength'},
    {'label': 'Petal Width', 'value': 'PetalWidth'}
]

app.layout = html.Div(
    style={'margin': -30},
    children=[
        html.Div(style={
            'position': 'absolute',
            'width': '100%',
            'height': '100%',
            'backgroundColor': colors['background']
        }),
        html.Div(
            className='container',
            style={'color': colors['text'], 'paddingTop': 60},
            children=[
                html.H1('New Colorscale: Cividis'),
                html.H4('Color Vision Deficiency Friendly and Perceptually Uniform'),
                html.Hr(),
                html.Div([
                    html.Div(className='three columns', children=[
                        html.Label('X Axis'),
                        dcc.RadioItems(
                            id='x',
                            options=options,
                            value='SepalLength',
                        ),
                        html.Hr(),
                        html.Label('Y Axis'),
                        dcc.RadioItems(
                            id='y',
                            options=options,
                            value='SepalWidth',
                        )
                    ]),
                    html.Div(className='nine columns', children=[dcc.Graph(id='cividis')])
                ])
            ]
        )
    ]
)


@app.callback(
    Output('cividis', 'figure'),
    [Input('x', 'value'), Input('y', 'value')])
def update_graph(x, y):
    return {
        'data': [{
            'x': df[x], 'y': df[y], 'type': 'histogram2dcontour',
            'scl': 'Cividis',
            'colorbar': {'bgcolor': colors['background']},
        }],
        'layout': {
            'font': {'color': colors['text']},
            'paper_bgcolor': colors['background'],
            'plot_bgcolor': colors['background'],
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0},
            'xaxis': {'ticks': '', 'showticklabels': False},
            'yaxis': {'ticks': '', 'showticklabels': False}
        }
    }

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
