import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div(id='my-output-interval'),
    dcc.Interval(id='my-interval', interval=500),
])


@app.callback(
    Output('my-output-interval', 'children'),
    [Input('my-interval', 'n_intervals')])
def display_output(n):
    return '{} have passed'.format(n)


if __name__ == '__main__':
    app.run_server(debug=True)
