import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from sqlalchemy import create_engine

# Create a simple database
engine = create_engine('sqlite:///sample.db')
df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5, 6],
    'b': ['x', 'y', 'x', 'x', 'z', 'y']
})
df.to_sql('dataframe', engine, if_exists='replace')

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
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df.b.unique()],
        value='x',
        clearable=False
    ),
    html.Div(id='table-container')
])


@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('dropdown', 'value')])
def sql(value):
    dff = pd.read_sql_query(
        'SELECT a, b FROM dataframe WHERE b = "{}"'.format(value),
        engine
    )
    return generate_table(dff)

if __name__ == '__main__':
    app.run_server(debug=True)
