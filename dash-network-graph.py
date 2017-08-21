import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State

import visdcc

app = dash.Dash()

app.layout = html.Div([
      visdcc.Network(id='net',
                     data={'nodes':[{'id': 1, 'label': 'Node 1', 'color':'#00ffff'},
                                    {'id': 2, 'label': 'Node 2'},
                                    {'id': 4, 'label': 'Node 4'},
                                    {'id': 5, 'label': 'Node 5'},
                                    {'id': 6, 'label': 'Node 6'}],
                             'edges':[{'id':'1-3', 'from': 1, 'to': 3},
                                      {'id':'1-2', 'from': 1, 'to': 2}]
                     },
                     options=dict(height='600px', width='100%')),
      dcc.RadioItems(id='color',
                     options=[{'label': 'Red'  , 'value': '#ff0000'},
                              {'label': 'Green', 'value': '#00ff00'},
                              {'label': 'Blue' , 'value': '#0000ff'}],
                     value='Red')
])

@app.callback(
    Output('net', 'options'),
    [Input('color', 'value')])
def myfun(x):
    return {'nodes':{'color': x}}

if __name__ == '__main__':
    app.run_server(debug=True)
