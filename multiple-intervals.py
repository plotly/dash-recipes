# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, Event, State

app = dash.Dash()
# app.config.supress_callback_exceptions=True
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

def getLayout():
    return html.Div([
        html.H1(id='Title1',children='Multiple intervals in a single page',style={'text-align':'center'}),
        html.Div(id='Title2', children='''
        Test multiple intervals in a single page.
        ''',style={'margin-bottom':'50px', 'text-align':'center'}),
        html.Div('Div1',id='div1'),
        html.Div('Div2',id='div2'),
        html.Div('Div3',id='div3'),
        dcc.Interval(
            id='interval-component-1',
            interval=500 # in milliseconds
        ),
        dcc.Interval(
            id='interval-component-2',
            interval=300 # in milliseconds
        ),
        dcc.Interval(
            id='interval-component-3',
            interval=400 # in milliseconds
        )
    ])

app.layout = getLayout

@app.callback(Output('div1', 'children'),
    events=[Event('interval-component-1', 'interval')],
    state=[State('div1', 'children')])
def update_div_1(origin):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', 'update_div_1')
    return origin+'.'


@app.callback(Output('div2', 'children'),
    events=[Event('interval-component-2', 'interval')],
    state=[State('div2', 'children')])
def update_div_2(origin):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', 'update_div_2')
    return origin+'.'

@app.callback(Output('div3', 'children'),
    events=[Event('interval-component-3', 'interval')],
    state=[State('div3', 'children')])
def update_div_2(origin):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', 'update_div_3')
    return origin+'.'


if __name__ == '__main__':
    app.run_server(debug=True, port=10091, host='0.0.0.0', processes=3)
