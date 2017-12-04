import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[],
        value=None
    ),
    html.Button('Add Option', id='button', n_clicks=0)
])


@app.callback(
    Output('dropdown', 'options'),
    [Input('button', 'n_clicks')],
    [State('dropdown', 'options')])
def update_options(n_clicks, existing_options):
    option_name = 'Option {}'.format(n_clicks)
    existing_options.append({'label': option_name, 'value': option_name})
    return existing_options


if __name__ == '__main__':
    app.run_server(debug=True)
