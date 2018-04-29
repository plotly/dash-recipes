import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime
from flask_caching import Cache
import os
import pandas as pd
import time
import uuid


app = dash.Dash()
cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'localhost:6379'),

    # Alternatively, save on the filesystem with the following config:
    # Note that filesystem cache doesn't work on systems with ephemeral
    # filesystems like Heroku.
    # 'CACHE_TYPE': 'filesystem',
    # 'CACHE_DIR': 'cache-directory',
    # should be equal to maximum number of users on the app at a single time
    # higher numbers will store more data in the filesystem / redis cache
    'CACHE_THRESHOLD': 200
})

def get_dataframe(session_id):
    @cache.memoize()
    def query_and_serialize_data(session_id):
        # expensive or user/session-unique data processing step goes here

        # simulate a user/session-unique data processing step by generating
        # data that is dependent on time
        now = datetime.datetime.now()

        # simulate an expensive data processing task by sleeping
        time.sleep(3)

        df = pd.DataFrame({
            'time': [
                str(now - datetime.timedelta(seconds=15)),
                str(now - datetime.timedelta(seconds=10)),
                str(now - datetime.timedelta(seconds=5)),
                str(now)
            ],
            'values': ['a', 'b', 'a', 'c']
        })
        return df.to_json()

    return pd.read_json(query_and_serialize_data(session_id))

def serve_layout():
    session_id = str(uuid.uuid4())

    return html.Div(style={'marginLeft': 80}, children=[
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        html.Button('Get data', id='button'),
        html.Div(id='output-1'),
        html.Div(id='output-2')
    ])

app.layout = serve_layout


@app.callback(Output('output-1', 'children'),
              [Input('button', 'n_clicks'),
               Input('session-id', 'children')])
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 1 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])



@app.callback(Output('output-2', 'children'),
              [Input('button', 'n_clicks'),
               Input('session-id', 'children')])
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 2 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
