import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import datetime
from flask_caching import Cache
import pandas as pd
import time

app = dash.Dash()
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

TIMEOUT = 10

def dataframe():
    @cache.memoize(timeout=TIMEOUT)
    def query_data():
        df = pd.DataFrame({'a': [datetime.datetime.now()]})
        return df.to_json()

    return pd.read_json(query_data())

def serve_layout():
    df = dataframe()
    return html.Div([
        html.Pre(df.to_json()),
        html.Hr(),
    ])


app.layout = serve_layout


if __name__ == '__main__':
    app.run_server(debug=True)
