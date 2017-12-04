import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

import time

app = dash.Dash()

app.layout = html.Div([
    html.Label([
        'Input 1',
        dcc.Input(id='input-1', type="text")
    ]),
    html.Label([
        'Input 2',
        dcc.Input(id='input-2', type="text"),
    ]),
    html.Label([
        'Input 3',
        dcc.Input(id='input-3', type="text"),
    ]),
    html.Button('Run Model', id='run-model', n_clicks=0),
    html.Div('(running the model can take several seconds)'),
    html.Hr(),
    html.Div(id='output')
], className="container")


@app.callback(
    Output('output', 'children'),
    [Input('run-model', 'n_clicks')],
    [State('input-1', 'value'),
     State('input-2', 'value'),
     State('input-3', 'value')])
def run_model(n_clicks, input1, input2, input3):
    if n_clicks == 0:
        return ''
    time.sleep(10)
    return (
        'Model completed: f("{}", "{}", "{}")'.format(
            input1, input2, input3
        )
    )


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Loading screen CSS
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})


if __name__ == '__main__':
    app.run_server(debug=True)
