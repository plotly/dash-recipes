# -*- coding: utf-8 -*-

import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div([
    html.Button(id='button-1', children='Button 1', n_clicks_timestamp=-1),
    html.Button(id='button-2', children='Button 2', n_clicks_timestamp=-1),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('button-1', 'n_clicks_timestamp'),
     Input('button-2', 'n_clicks_timestamp')]
)
def update_output(b1_timestamp, b2_timestamp):
    if b1_timestamp > b2_timestamp:
        return '''
            Button 1 Was Clicked
            (Button 1 timestamp: {}. Button 2 timestamp: {}.)
        '''.format(b1_timestamp, b2_timestamp)
    else:
        return '''
            Button 2 Was Clicked
            (Button 1 timestamp: {}. Button 2 timestamp: {}.)
        '''.format(b1_timestamp, b2_timestamp)


if __name__ == '__main__':
    app.run_server(debug=True)
