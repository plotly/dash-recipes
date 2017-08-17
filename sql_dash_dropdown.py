import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from sqlalchemy import create_engine

ENGINE = create_engine('sqlite:///sample.db')

# Create a simple database
def create_sample_database():

    df = pd.DataFrame({
        'column_a': [1, 2, 3, 4, 5, 6],
        'column_b': [6, 5, 4, 3, 2, 1],
        'column_c': ['a', 'b', 'c', 'a', 'a', 'b']
    })
    df.to_sql('dataframe', ENGINE, if_exists='replace')


create_sample_database()


# Dash
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app = dash.Dash()
app.layout = html.Div([
    dcc.Input(
        id='sql-query',
        value='SELECT * FROM dataframe',
        style={'width': '100%'},
        type='text'
    ),
    html.Button('Run Query', id='run-query'),

    html.Hr(),

    html.Div([
        html.Div(id='table-container', className="four columns"),

        html.Div([
            html.Div([
                html.Div([
                    html.Label('Select X'),
                    dcc.Dropdown(
                        id='dropdown-x',
                        clearable=False,
                    )
                ], className="six columns"),
                html.Div([
                    html.Label('Select Y'),
                    dcc.Dropdown(
                        id='dropdown-y',
                        clearable=False,
                    )
                ], className="six columns")
            ], className="row"),
            html.Div(dcc.Graph(id='graph'), className="ten columns")
        ], className="eight columns")
    ], className="row"),

    # hidden store element
    html.Div(id='table-store', style={'display': 'none'})
])


@app.callback(
    dash.dependencies.Output('table-store', 'children'),
    [dash.dependencies.Input('run-query', 'n_clicks')],
    state=[dash.dependencies.State('sql-query', 'value')])
def sql(number_of_times_button_has_been_clicked, sql_query):
    dff = pd.read_sql_query(
        sql_query,
        ENGINE
    )
    return dff.to_json()


@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('table-store', 'children')])
def dff_to_table(dff_json):
    dff = pd.read_json(dff_json)
    return generate_table(dff)


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('table-store', 'children'),
     dash.dependencies.Input('dropdown-x', 'value'),
     dash.dependencies.Input('dropdown-y', 'value')])
def dff_to_table(dff_json, dropdown_x, dropdown_y):
    dff = pd.read_json(dff_json)
    return {
        'data': [{
            'x': dff[dropdown_x],
            'y': dff[dropdown_y],
            'type': 'bar'
        }],
        'layout': {
            'margin': {
                'l': 20,
                'r': 10,
                'b': 60,
                't': 10
            }
        }
    }


@app.callback(
    dash.dependencies.Output('dropdown-x', 'options'),
    [dash.dependencies.Input('table-store', 'children')])
def create_options_x(dff_json):
    dff = pd.read_json(dff_json)
    return [{'label': i, 'value': i} for i in dff.columns]


@app.callback(
    dash.dependencies.Output('dropdown-y', 'options'),
    [dash.dependencies.Input('table-store', 'children')])
def create_options_y(dff_json):
    dff = pd.read_json(dff_json)
    return [{'label': i, 'value': i} for i in dff.columns]


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
