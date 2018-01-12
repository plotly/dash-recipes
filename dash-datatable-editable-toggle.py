import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt

app = dash.Dash()
app.layout = html.Div([
    dcc.RadioItems(
        id='toggle-editable',
        options=[
            {'label': 'Editable', 'value': True},
            {'label': 'Non-Editable', 'value': False},
        ],
        value=True
    ),
    dt.DataTable(
        id='datatable',
        rows=[{'x': 1, 'y': 3}, {'x': 5, 'y': 1}],
    )
])

@app.callback(
    Output('datatable', 'editable'),
    [Input('toggle-editable', 'value')])
def update_editable(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)
