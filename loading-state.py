import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import time

app = dash.Dash()

app.layout = html.Div([
    html.H3('Loading State Example'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['a', 'b', 'c']]
    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('dropdown', 'value')])
def update_value(value):
    time.sleep(2)
    return 'You have computed {}'.format(value)

# Dash CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# Loading screen CSS
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
