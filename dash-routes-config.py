# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import csv
from datetime import datetime as dt

app = dash.Dash(__name__)
app.config.update({
    #'url_base_pathname': '/showtemperature1/',
    # as the proxy server will remove the prefix
    'routes_pathname_prefix': '/showtemperature2/',

    # the front-end will prefix this string to the requests
    # that are made to the proxy server
    'requests_pathname_prefix': '/pompidom3/'
})
server = app.server

app.layout = html.Div([])

if __name__ == '__main__':
    app.run_server(debug=True)
