import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from flask import send_from_directory
import json
import pandas as pd
import numpy as np
import os
import plotly

app = dash.Dash()
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

ROWS = [
    {'a': 'AA', 'b': 1},
    {'a': 'AB', 'b': 2},
    {'a': 'BB', 'b': 3},
    {'a': 'BC', 'b': 4},
    {'a': 'CC', 'b': 5},
    {'a': 'CD', 'b': 6}
]


app.layout = html.Div([
    html.Link(rel='stylesheet', href='/static/dash-datatable.css'),

    dt.DataTable(
        rows=ROWS,

        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='datatable'
    ),
    html.Div(id='selected-indexes'),
    dcc.Graph(
        id='graph-gapminder'
    ),
], className="container")


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


if __name__ == '__main__':
    app.run_server(debug=True)
