# -*- coding: utf-8 -*-

import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div([
    html.Button(id='button-1', children='Button 1', n_clicks=0),
    html.Button(id='button-2', children='Button 2', n_clicks=0),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('button-1', 'n_clicks'),
     Input('button-2', 'n_clicks')],
    [State('button-1', 'n_clicks'),
     State('button-2', 'n_clicks')])
def update_output(b1_clicks, b2_clicks, prev_b1_clicks, prev_b2_clicks):
    if b1_clicks > prev_b1_clicks:
        return '''
            Button 1 Was Clicked
            (Button 1: {} → {} clicks. Button 2: {} → {} clicks.)
        '''.format(prev_b1_clicks, b1_clicks, prev_b2_clicks, b2_clicks)
    else:
        return '''
            Button 2 Was Clicked
            (Button 1: {} → {} clicks. Button 2: {} → {} clicks.)
        '''.format(prev_b1_clicks, b1_clicks, prev_b2_clicks, b2_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
