# -*- coding: utf-8 -*-

import dash
import dash_html_components as html
import dash_core_components as dcc

print(dcc.__version__)

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        options=[
            {'label': 'Montréal', 'value': 'Montréal'},
            {'label': 'Tokyo', 'value': 'Tokyo'},
            {'label': '北京', 'value': '北京'},
        ]
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
