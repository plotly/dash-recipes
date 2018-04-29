import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_dangerously_set_inner_html
import dash_html_components as html
import dash_table_experiments as dt

app = dash.Dash()

app.layout = html.Div([

    dcc.Location(id='url'),

    html.Div(id='container'),


    # and then a div with examples of all of the other component suites in it

    html.Div(style={'display': 'none'}, children=[

        dt.DataTable(rows=[{}]),

        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('')

    ])

])


# Render different pages inside this function
@app.callback(Output('container', 'children'), [Input('url', 'href')])
def display_content(href):
    return html.Div([
        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('<h1>App</h1>'),
        dt.DataTable(rows=[{'a': 1, 'b': 3}])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
