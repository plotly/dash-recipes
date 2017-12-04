import copy
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import json
import pandas as pd
import plotly

app = dash.Dash()

app.scripts.config.serve_locally = True

RECORDS = [
    {'Input': '', 'Output': ''}
    for i in range(100)
]

app.layout = html.Div([
    html.H4('Editable DataTable'),
    html.Div([
        html.Div(
            children=dt.DataTable(
                rows=RECORDS,

                # optional - sets the order of columns
                columns=['Input', 'Output'],

                editable=True,

                id='editable-table'
            ),
            className='six columns'
        ),
        html.Pre(id='output', className='six columns')
    ])
], className='container')


@app.callback(
    Output('output', 'children'),
    [Input('editable-table', 'row_update'),
     Input('editable-table', 'rows')])
def display_output(row_update, rows):
    return html.Div(className='row', children=[
        html.Div([
            html.Code('row_update'),
            html.Pre(json.dumps(row_update, indent=2))
        ], className='six columns'),
        html.Div([
            html.Code('rows'),
            html.Pre(json.dumps(rows, indent=2))
        ], className='six columns'),
    ])


@app.callback(
    Output('editable-table', 'rows'),
    [Input('editable-table', 'row_update')],
    [State('editable-table', 'rows')])
def update_rows(row_update, rows):
    row_copy = copy.deepcopy(rows)
    if row_update:
        updated_row_index = row_update[0]['from_row']
        updated_value = row_update[0]['updated'].values()[0]
        row_copy[updated_row_index]['Output'] = (
            float(updated_value) ** 2
        )
    return row_copy


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
