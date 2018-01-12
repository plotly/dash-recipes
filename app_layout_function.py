import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

print('App start')


def serve_layout():
    print('Calling layout')
    return html.Div([
        html.Div(id='output-1'),
        html.Div(id='output-2'),
        dcc.Dropdown(
            id='input', options=[{
                'label': i,
                'value': i
            } for i in ['a', 'b']])
    ])


app.layout = serve_layout


@app.callback(Output('output-1', 'children'), [Input('input', 'value')])
def update_outout(value):
    return 'You have selected {}'.format(value)


@app.callback(Output('output-2', 'children'), [Input('input', 'value')])
def update_outout(value):
    return 'You have selected {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=False)
