import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import json

app = dash.Dash()
app.layout = html.Div([
    dt.DataTable(
        id='datatable',
        rows=[
            {'x': 1, 'y': 3},
            {'x': 2, 'y': 10}
        ],
        columns=['x']
        filterable=True,
        filters={
          "x": {
            "column": {
              "sortable": True,
              "name": "x",
              "filterable": True,
              "editable": True,
              "width": 673,
              "rowType": "filter",
              "key": "x",
              "left": 673
            },
            "filterTerm": "2"
          }
        }
    ),
    html.Div(id='content')
])


@app.callback(Output('content', 'children'), [Input('datatable', 'filters')])
def display_filters(filters):
    return html.Pre(json.dumps(filters, indent=2))


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
