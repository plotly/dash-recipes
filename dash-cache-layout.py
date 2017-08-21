import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import datetime
import os
from flask_caching import Cache


app = dash.Dash(__name__)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache'
})
app.config.supress_callback_exceptions = True

timeout = 20

@cache.memoize(timeout=timeout)
def compute_expensive_data():
    return str(datetime.datetime.now())


def generate_layout():
    expensive_data = compute_expensive_data()
    return html.Div([
        html.H3('Last updated at: ' + expensive_data),
        html.Div(id='flask-cache-memoized-children'),
        dcc.RadioItems(
            id='flask-cache-memoized-dropdown',
            options=[
                {'label': 'Option {}'.format(i), 'value': 'Option {}'.format(i)}
                for i in range(1, 4)
            ],
            value='Option 1'
        ),
        html.Div('Results are cached for {} seconds'.format(timeout))
    ])

app.layout = generate_layout


@app.callback(
    Output('flask-cache-memoized-children', 'children'),
    [Input('flask-cache-memoized-dropdown', 'value')])
@cache.memoize(timeout=timeout)
def render(value):
    return 'Selected "{}" at "{}"'.format(
        value, datetime.datetime.now().strftime('%H:%M:%S')
    )


if __name__ == '__main__':
    app.run_server(debug=True)
