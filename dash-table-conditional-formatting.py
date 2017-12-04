import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))

COLORS = [
    {
        'background': '#fef0d9',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#fdcc8a',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#fc8d59',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#d7301f',
        'text': 'rgb(30, 30, 30)'
    },
]


def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def cell_style(value, min_value, max_value):
    style = {}
    if is_numeric(value):
        relative_value = (value - min_value) / (max_value - min_value)
        if relative_value <= 0.25:
            style = {
                'backgroundColor': COLORS[0]['background'],
                'color': COLORS[0]['text']
            }
        elif relative_value <= 0.5:
            style = {
                'backgroundColor': COLORS[1]['background'],
                'color': COLORS[1]['text']
            }
        elif relative_value <= 0.75:
            style = {
                'backgroundColor': COLORS[2]['background'],
                'color': COLORS[2]['text']
            }
        elif relative_value <= 1:
            style = {
                'backgroundColor': COLORS[3]['background'],
                'color': COLORS[3]['text']
            }
    return style


def generate_table(dataframe, max_rows=100):
    max_value = df.max(numeric_only=True).max()
    min_value = df.min(numeric_only=True).max()
    rows = []
    for i in range(min(len(dataframe), max_rows)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            style = cell_style(value, min_value, max_value)
            row.append(html.Td(value, style=style))
        rows.append(html.Tr(row))

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        rows)


app = dash.Dash()
app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

app.layout = html.Div(children=[
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
