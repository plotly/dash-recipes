import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np

app = dash.Dash()

value_range = [-5, 5]

app.layout = html.Div([
    html.Div([
        html.Div(dcc.Graph(animate=True, id='graph-1'), className="six columns"),
        html.Div(dcc.Graph(animate=True, id='graph-2'), className="six columns")
    ], className="row"),
    dcc.RangeSlider(
        id='slider',
        min=value_range[0],
        max=value_range[1],
        step=1,
        value=[-2, 2],
        marks={i: i for i in range(value_range[0], value_range[1]+1)}
    )
], className="container")

trace = {
    'mode': 'markers',
    'marker': {
        'size': 12,
        'opacity': 0.5,
        'line': {
            'width': 0.5,
            'color': 'white'
        }
    }
}

@app.callback(
    dash.dependencies.Output('graph-1', 'figure'),
    [dash.dependencies.Input('slider', 'value')])
def update_graph_1(value):
    x = np.random.rand(50) * (value[1] - value[0]) + value[0]
    y = np.random.rand(50) * (value[1] - value[0]) + value[0]
    return {
        'data': [dict({'x': x, 'y': y}, **trace)],
        'layout': {
            'xaxis': {'range': [np.min(x), np.max(x)]},
            'yaxis': {'range': [np.min(y), np.max(y)]}
        }
    }

@app.callback(
    dash.dependencies.Output('graph-2', 'figure'),
    [dash.dependencies.Input('slider', 'value')])
def update_graph_1(value):
    x = np.random.rand(50) * (value[1] - value[0]) + value[0]
    y = np.random.rand(50) * (value[1] - value[0]) + value[0]
    return {
        'data': [dict({'x': x, 'y': y}, **trace)],
        'layout': {
            'xaxis': {'range': value_range},
            'yaxis': {'range': value_range}
        }
    }

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
