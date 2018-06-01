# https://community.plot.ly/t/dash-interval-updates-issues/7015/8

import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.RadioItems(
        id='variable_selected',
        options=[
            {'label':'Choice 1','value': 'option-1'},
            {'label':'Choice 2','value': 'option-2'},
            {'label':'Choice 3','value': 'option-3'}
        ],
        value='option-1'
    ),
    dcc.Interval(id='update_interval', interval=2000, n_intervals=0),
    html.Div(id='output_example')
])


@app.callback(
    Output('output_example', 'children'),
    [Input('update_interval', 'n_intervals'),
     Input('variable_selected', 'value')])
def test(interval, value):
    return "The interval number is {} and the value is {}".format(
        interval, value
    )


if __name__ == '__main__':
    app.run_server(debug=True,port=8055)
