import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime

app = dash.Dash()

app.layout = html.Div([
    html.Div(id='my-output-interval'),
    dcc.Interval(id='my-interval', interval=5),
])


@app.callback(
    Output('my-output-interval', 'children'),
    [Input('my-interval', 'n_intervals')])
def display_output(n):
    now = datetime.datetime.now()
    return '{} intervals have passed. It is {}:{}:{}'.format(
        n,
        now.hour,
        now.minute,
        now.second
    )


if __name__ == '__main__':
    app.run_server(debug=True)
