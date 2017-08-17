import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.Button('Click Me', id='button'),
    html.H3(id='button-clicks'),

    html.Hr(),

    html.Label('Input 1'),
    dcc.Input(id='input-1'),

    html.Label('Input 2'),
    dcc.Input(id='input-2'),

    html.Label('Slider 1'),
    dcc.Slider(id='slider-1'),

    html.Button('Click Me', id='button-2'),

    html.Div(id='output')
], className='container')

@app.callback(
    Output('button-clicks', 'children'),
    [Input('button', 'n_clicks')])
def clicks(n_clicks):
    return 'Button has been clicked {} times'.format(n_clicks)

@app.callback(
    Output('output', 'children'),
    [Input('button-2', 'n_clicks')],
    state=[State('input-1', 'value'),
     State('input-2', 'value'),
     State('slider-1', 'value')])
def compute(n_clicks, input1, input2, slider1):
    return 'A computation based off of {}, {}, and {}'.format(
        input1, input2, slider1
    )


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


if __name__ == '__main__':
    app.run_server(debug=True)
