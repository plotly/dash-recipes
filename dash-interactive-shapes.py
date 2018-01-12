import json
from textwrap import dedent as d
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/dZVMbK.css'})

styles = {'pre': {'border': 'thin lightgrey solid', 'overflowX': 'scroll'}}

app.layout = html.Div(className='row', children=[
    dcc.Graph(
        id='basic-interactions',
        className='six columns',
        figure={
            'data': [{
                'x': [1, 2, 3, 4],
                'y': [4, 1, 3, 5],
                'text': ['a', 'b', 'c', 'd'],
                'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                'name': 'Trace 1',
                'mode': 'markers',
                'marker': {
                    'size': 12
                }
            }, {
                'x': [1, 2, 3, 4],
                'y': [9, 4, 1, 4],
                'text': ['w', 'x', 'y', 'z'],
                'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
                'name': 'Trace 2',
                'mode': 'markers',
                'marker': {
                    'size': 12
                }
            }],
            'layout': {
                'shapes': [{
                    'type': 'line',

                    'x0': 0,
                    'x1': 1,
                    'xref': 'paper',

                    'y0': 3,
                    'y1': 3,
                    'yref': 'y',

                    'line': {
                        'width': 4,
                        'color': 'rgb(30, 30, 30)'
                    }
                }]
            }
        },
        config={
            'editable': True,
            'edits': {
                'shapePosition': True
            }
        }
    ),
    html.Div(
        className='six columns',
        children=[
            html.Div(
                [
                    dcc.Markdown(
                        d("""
                **Zoom and Relayout Data**

            """)),
                    html.Pre(id='relayout-data', style=styles['pre']),
                ]
            )
        ]
    )
])


@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def display_selected_data(relayoutData):
    return json.dumps(relayoutData, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)
