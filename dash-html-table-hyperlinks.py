import dash
import dash_html_components as html
import pandas as pd

df = pd.DataFrame({
    'id': ['a', 'b', 'c', 'd'],
    'col1': [1, 2, 3, 4]
})

def Table(dataframe):
    rows = []
    for i in range(len(dataframe)):
        row = []
        for col in dataframe.columns:
            value = dataframe.iloc[i][col]
            # update this depending on which
            # columns you want to show links for
            # and what you want those links to be
            if col == 'id':
                cell = html.Td(html.A(href=value, children=value))
            else:
                cell = html.Td(children=value)
            row.append(cell)
        rows.append(html.Tr(row))
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        rows
    )

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/dZVMbK.css'})

app.layout = html.Div(children=[
    Table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
