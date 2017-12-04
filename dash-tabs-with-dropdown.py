import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div([
    dcc.Tabs(
        tabs=[
            {'label': 'Market Value', 'value': 1},
            {'label': 'Usage Over Time', 'value': 2},
            {'label': 'Predictions', 'value': 3},
            {'label': 'Target Pricing', 'value': 4},
        ],
        value=3,
        id='tabs'
    ),
    html.Div(id='tab-output')
], style={
    'width': '80%',
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto'
})


@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
def update_output(value):
    return html.Div([
        dcc.Dropdown(options=[
            {'label': i, 'value': i} for i in range(5)
        ])
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
