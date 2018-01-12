import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime
from flask_caching import Cache
import pandas as pd
import time
import uuid

app = dash.Dash()
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 50  # should be equal to maximum number of active users
})

@cache.memoize()
def query_data(session_id):
    df = pd.DataFrame({'a': [datetime.datetime.now()]})
    return df.to_json()


def dataframe(session_id):
    return pd.read_json(query_data(session_id))

def serve_layout():
    session_id = str(uuid.uuid4())
    df = dataframe(session_id)
    return html.Div([
        html.Div(session_id, id='session-id', style={'display': 'none'}),
        dcc.Dropdown(id='dropdown', value='a', options=[
            {'label': i, 'value': i} for i in ['a', 'b', 'c', 'd']
        ]),
        html.Pre(id='output')
    ])

app.layout = serve_layout


@app.callback(Output('output', 'children'),
              [Input('dropdown', 'value'),
               Input('session-id', 'children')])
def display_value(value, session_id):
    df = dataframe(session_id)
    return df.to_csv()


if __name__ == '__main__':
    app.run_server(debug=True)
