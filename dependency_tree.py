import numpy as np
import dash
from dash.dependencies import Input, Output
from plotly.graph_objs import *
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
# function to plot
def func(x):
    return x[:,0]**2 + np.sin(x[:,1])
# default ranges for x0 & x1
xranges = [[0,1], [-np.pi, np.pi]]
# dropdown to pick which x to plot against
xchooser = dcc.Dropdown(
        id='xchooser',
        options=[{'label':'x0', 'value':'0'},{'label':'x1', 'value':'1'}],
        value='0')
# the user can also modify the ranges manually
minsetter = dcc.Input(id='minsetter', type='number', value=xranges[0][0])
maxsetter = dcc.Input(id='maxsetter', type='number', value=xranges[0][1])

app.layout = html.Div([
        html.Div(xchooser, style={'width':'15%'}),
        html.Div(['Min: ',minsetter,'Max: ',maxsetter]),
        html.Div([dcc.Graph(id='trend_plot')], style={'width':'80%','float':'right'})
    ])

@app.callback(Output('minsetter','value'),[Input('xchooser','value')])
def set_min(xindex):
    return xranges[int(xindex)][0]
@app.callback(Output('maxsetter','value'),[Input('xchooser','value')])
def set_max(xindex):
    return xranges[int(xindex)][1]
@app.callback(Output('trend_plot','figure'),
        [Input('xchooser','value'),Input('minsetter','value'),Input('maxsetter','value')])
def make_graph(xindex, xmin, xmax):
    npt = 20
    xgrid = np.zeros((npt,2))
    xgrid[:,int(xindex)] = np.linspace(int(xmin), int(xmax), npt)
    print('Calling func!')
    f = func(xgrid)
    return Figure(data=[Scatter(x=xgrid[:,int(xindex)], y=f, mode='markers+lines')])

if __name__ == '__main__':
    app.run_server()
