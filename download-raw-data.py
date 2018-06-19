import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from six.moves.urllib.parse import quote


df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [2, 1, 5, 6],
    'c': ['x', 'x', 'y', 'y']
})


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash(__name__)
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
app.layout = html.Div([
    html.Label('Filter'),

    dcc.Dropdown(
        id='field-dropdown',
        options=[
            {'label': i, 'value': i} for i in
            (['all'] + list(df['c'].unique()))],
        value='all'
    ),
    html.Div(id='table'),
    html.A(
        'Download Data',
        id='download-link',
        download="rawdata.csv",
        href="",
        target="_blank"
    )
])


def filter_data(value):
    if value == 'all':
        return df
    else:
        return df[df['c'] == value]


@app.callback(
    dash.dependencies.Output('table', 'children'),
    [dash.dependencies.Input('field-dropdown', 'value')])
def update_table(filter_value):
    dff = filter_data(filter_value)
    return generate_table(dff)


@app.callback(
    dash.dependencies.Output('download-link', 'href'),
    [dash.dependencies.Input('field-dropdown', 'value')])
def update_download_link(filter_value):
    dff = filter_data(filter_value)
    csv_string = dff.to_csv(index=False, encoding='utf-8')
    csv_string = "data:text/csv;charset=utf-8,%EF%BB%BF" + quote(csv_string)
    return csv_string


if __name__ == '__main__':
    app.run_server(debug=True)
