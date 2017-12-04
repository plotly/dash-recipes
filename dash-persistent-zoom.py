import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import copy

app = dash.Dash()

FIGURE = {
    'data': [{
        'x': [1, 2, 3],
        'y': [4, 3, 6],
        'mode': 'markers',
        'marker': {
            'size': 8
        }
    }],
    'layout': {
        'xaxis': {},
        'yaxis': {},
    }
}

app.layout = html.Div([
    html.H3('Persistent Zoom on Updates'),
    html.Div('''
        Try zooming into the graph (clicking and dragging on the graph),
        then updating the text box. Notice how the graph does not zoom out
        when the graph is updated. Switching to "Refresh View" will
        redraw the graph with auto-range enabled.
    '''),
    dcc.Input(id='my-input'),
    dcc.RadioItems(
        id='lock-zoom',
        options=[{'label': i, 'value': i} for i in ['Lock View', 'Refresh View']],
        value='Lock View'
    ),
    dcc.Graph(
        id='my-graph',
        figure=FIGURE
    )
])

@app.callback(
    Output('my-graph', 'figure'),
    [Input('my-input', 'value'),
     Input('lock-zoom', 'value')],
    [State('my-graph', 'relayoutData')])
def update_graph(value, lock_zoom, relayout_data):
    new_figure = copy.deepcopy(FIGURE)
    new_figure['layout']['title'] = value

    # relayout_data contains data on the zoom and range actions
    print(relayout_data)
    if relayout_data and lock_zoom == 'Lock View':
        if 'xaxis.range[0]' in relayout_data:
            new_figure['layout']['xaxis']['range'] = [
                relayout_data['xaxis.range[0]'],
                relayout_data['xaxis.range[1]']
            ]
        if 'yaxis.range[0]' in relayout_data:
            new_figure['layout']['yaxis']['range'] = [
                relayout_data['yaxis.range[0]'],
                relayout_data['yaxis.range[1]']
            ]

    return new_figure

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
