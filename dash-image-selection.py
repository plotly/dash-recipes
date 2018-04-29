import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import base64
import json

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/dZVMbK.css'})

RANGE = [0, 1]

def InteractiveImage(id, image_path):
    encoded_image = base64.b64encode(open(image_path, 'rb').read())
    return dcc.Graph(
        id=id,
        figure={
            'data': [],
            'layout': {
                'xaxis': {
                    'range': RANGE
                },
                'yaxis': {
                    'range': RANGE,
                    'scaleanchor': 'x',
                    'scaleratio': 1
                },
                'height': 600,
                'images': [{
                    'xref': 'x',
                    'yref': 'y',
                    'x': RANGE[0],
                    'y': RANGE[1],
                    'sizex': RANGE[1] - RANGE[0],
                    'sizey': RANGE[1] - RANGE[0],
                    'sizing': 'stretch',
                    'layer': 'below',
                    'source': 'data:image/png;base64,{}'.format(encoded_image)
                }],
                'dragmode': 'select'  # or 'lasso'
            }
        }
    )


app.layout = html.Div([
    html.Div(className='row', children=[
        html.Div(InteractiveImage('image', 'dash_app.png'), className='six columns'),
        html.Div(dcc.Graph(id='graph'), className='six columns')
    ]),
    html.Pre(id='console')
])


# display the event data for debugging
@app.callback(Output('console', 'children'), [Input('image', 'selectedData')])
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@app.callback(Output('graph', 'figure'), [Input('image', 'selectedData')])
def update_histogram(selectedData):
    x_range = selectedData['range']['x']
    x_range = selectedData['range']['y']
    # filter data based off of selection in here

    # for simple example purposes, we'll just display the selected RANGE
    return {
        'data': [{
            'x': x_range,
            'y': x_range,
            'mode': 'markers',
            'marker': {
                'size': 20
            }
        }],
        'layout': {
            'xaxis': {'range': RANGE},
            'yaxis': {'range': RANGE, 'scaleanchor': 'x', 'scaleratio': 1},
            'height': 600
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
