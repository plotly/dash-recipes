import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash_table_experiments import DataTable
import json

app = dash.Dash()
app.config['suppress_callback_exceptions'] = True
app.layout = html.Div([
    html.Button(id='button', n_clicks=0, children='Show table'),
    html.Div(id='content'),
    html.Div(DataTable(rows=[{}]), style={'display': 'none'})
])


@app.callback(Output('content', 'children'), [Input('button', 'n_clicks')])
def display_output(n_clicks):
    if n_clicks > 0:
        return html.Div([
            html.Div(id='datatable-output'),
            DataTable(
                id='datatable',
                rows=[{'Column 1': i} for i in range(5)]
            )
        ])


@app.callback(
    Output('datatable-output', 'children'),
    [Input('datatable', 'rows')])
def update_output(rows):
    return html.Pre(
        json.dumps(rows, indent=2)
    )


if __name__ == '__main__':
    app.run_server(debug=True)
