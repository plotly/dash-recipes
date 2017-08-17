import dash_core_components as dcc
import dash_html_components as html
import dash
import datetime

app = dash.Dash()

app.layout = html.Div([
    dcc.Interval(id='my-interval'),
    dcc.RadioItems(id='set-time',
        value=1000,
        options=[
            {'label': 'Every second', 'value': 1000},
            {'label': 'Every 5 seconds', 'value': 5000},
            {'label': 'Off', 'value': 60*60*1000} # or just every hour
        ]),
    html.Div(id='display-time')
])


@app.callback(
    dash.dependencies.Output('display-time', 'children'),
    events=[dash.dependencies.Event('my-interval', 'interval')])
def display_time():
    return str(datetime.datetime.now())


@app.callback(
    dash.dependencies.Output('my-interval', 'interval'),
    [dash.dependencies.Input('set-time', 'value')])
def update_interval(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)
