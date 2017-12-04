import dash
import dash_core_components as dcc
import dash_html_components as html

import flask
import gevent
import os
import pandas as pd
from psycogreen.gevent import patch_psycopg
import sqlalchemy
import sqlalchemy_gevent
import time


server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
server.secret_key = os.environ.get('secret_key', 'secret')

engine = sqlalchemy.create_engine(
    '{dialect}://{username}:{password}@{host}:{port}/{schema}'.format(
        dialect='postgres',
        username='masteruser',
        password='connecttoplotly',
        host='readonly-test-postgres.cwwxgcilxwxw.us-west-2.rds.amazonaws.com',
        port=5432,
        schema='plotly_datasets'
    )
)

engine.pool._use_threadlocal = True

app.layout = html.Div([
    html.Button('Add a CPU bound request', id='cpu-click', n_clicks=0),
    html.Output(id='cpu-container'),

    html.Button('Add a IO bound request', id='io-click', n_clicks=0),
    html.Output(id='io-container'),

    html.Button('gevent sleep', id='gevent-sleep-click', n_clicks=0),
    html.Output(id='gevent-sleep-container'),
])


@app.callback(
    dash.dependencies.Output('cpu-container', 'children'),
    [dash.dependencies.Input('cpu-click', 'n_clicks')])
def process(n_clicks):
    print("Processing cpu request #{}".format(n_clicks))
    time.sleep(10)
    return 'Done (request #{})'.format(n_clicks)


@app.callback(
    dash.dependencies.Output('io-container', 'children'),
    [dash.dependencies.Input('io-click', 'n_clicks')])
def process(n_clicks):
    print("Processing io request #{}".format(n_clicks))
    pd.read_sql('SELECT pg_sleep(10)', engine)
    return 'Done (request #{})'.format(n_clicks)


@app.callback(
    dash.dependencies.Output('gevent-sleep-container', 'children'),
    [dash.dependencies.Input('gevent-sleep-click', 'n_clicks')])
def process(n_clicks):
    print("Processing gevent sleep request #{}".format(n_clicks))
    gevent.sleep(10)
    return 'Done (request #{})'.format(n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
