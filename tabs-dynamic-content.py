import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

app = dash.Dash()

app.layout = html.Div([
        html.Div([dcc.Dropdown(
                 id='dropdown',
                 options=[{'label': 'Option 1', 'value': 1},
                          {'label': 'Option 2', 'value': 2}],
                 value='1',
                 )]),
        dcc.Tabs(tabs=[{'label': 'Tab 1', 'value': 1},
                       {'label': 'Tab 2', 'value': 2}],
                 value=3,
                 id='tabs',
                 ),
        html.Div(id='tab-output')
    ])


@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
def display_content(value):
    if value == 1:
        return html.Div([dcc.Graph(id='graph')]) #etc. etc.
    elif value == 2:
        return html.Div([dt.DataTable(id='table')]) #etc. etc.


@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value')])
def update_graph(value):
    return something
    # callback that does something to graph


@app.callback(Output('datatable', 'rows'), [Input('dropdown', 'value')])
def update_graph(value):
    return something
    # callback that does something to table


if __name__ == '__main__':
    app.run_server(debug=True)
