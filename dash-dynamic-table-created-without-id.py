import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt

import json

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True

app.config['suppress_callback_exceptions'] = True
app.layout = html.Div([
    html.Button(
        id='display-content',
        children='Display Content',
        n_clicks=0
    ),
    html.Div(id='container'),
    dcc.RadioItems(),
    html.Div([
        dt.DataTable(rows=[{'Loading': ''}], id='dummy_table'),
        dcc.Input(id='dummy_input', value='')
    ], id='hidden-table', style={'display': 'none'})
])


@app.callback(
    Output('container', 'children'),
    [Input('display-content', 'n_clicks')])
def display_output(n_clicks):
    print('display_output ' + str(n_clicks))
    if n_clicks == 0:
        return ''
    return html.Div([
        html.Div([
            dcc.Input(
                value='Input {}'.format(i),
                id='input-{}'.format(i)
            )
            for i in range(10)
        ]),
        dt.DataTable(
            rows=[{'Loading': ''}],
            id='new-table'),
        html.Div(id='dynamic-output')
    ])


@app.callback(
    Output('dynamic-output', 'children'),
    [Input('input-{}'.format(i), 'value') for i in range(10)])
def dynamic_output(*args):
    print('update_children ')
    return json.dumps(args, indent=2)


@app.callback(
    Output('new-table', 'rows'),
    [Input('input-{}'.format(i), 'value') for i in range(10)])
def dynamic_output(*args):
    return [{'data': i, 'value': a} for (i, a) in enumerate(args)]


if __name__ == '__main__':
    app.run_server(debug=True)
