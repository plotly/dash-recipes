import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.config.supress_callback_exceptions = True

app.layout = html.Div([
    html.Button('Add a slider', id='button', n_clicks=0),
    html.Div(id='slider-container'),

    # this is a hack: include a hidden dcc component so that 
    # dash registers and serve's this component's JS and CSS 
    # libraries 
    dcc.Input(style={'display': 'none'})
])

@app.callback(Output('slider-container', 'children'), [Input('button', 'n_clicks')])
def add_sliders(n_clicks):
    return html.Div(
        [html.Div([
		html.Div(dcc.Slider(id='slider-{}'.format(i))),
	        html.Div(id='output-{}'.format(i), style={'marginTop': 30})
	]) for i in range(n_clicks)]
    )

# up to 10 sliders
for i in range(10):
    @app.callback(Output('slider-{}'.format(i), 'children'), [Input('slider-{}'.format(i), 'value')])
    def update_output(slider_i_value):
        return slider_i_value

if __name__ == '__main__':
    app.run_server(debug=True)
