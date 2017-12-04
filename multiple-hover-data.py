import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
    html.Div([
        html.Div(dcc.Graph(id='graph-1', figure={
            'data': [{
                'x': [1, 2, 3],
                'y': [4, 1, 5],
                'mode': 'markers',
                'marker': {
                    'size': 12
                }
            }]
        }), className="six columns"),
        html.Div(dcc.Graph(id='graph-2', figure={
            'data': [{
                'x': [1, 2, 3],
                'y': [2, 5, 10],
                'mode': 'markers',
                'marker': {
                    'size': 12
                }
            }]
        }), className="six columns"),
    ], className="row"),
    html.Div(id='container')
])


@app.callback(Output('graph-1', 'hoverData'), events=[Event('graph-2', 'hover')])
def resetHoverData1():
    return None


@app.callback(Output('graph-2', 'hoverData'), events=[Event('graph-1', 'hover')])
def resetHoverData2():
    return None


@app.callback(Output('container', 'children'),
              [Input('graph-1', 'hoverData'),
               Input('graph-2', 'hoverData')])
def updateContent(hoverData1, hoverData2):
    print(hoverData1)
    print(hoverData2)
    if hoverData1 is not None:
        return html.Div([
            html.Div('Graph 1'),
            html.Pre(hoverData1)
        ])
    if hoverData2 is not None:
        return html.Div([
            html.Div('Graph 2'),
            html.Pre(hoverData1)
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
