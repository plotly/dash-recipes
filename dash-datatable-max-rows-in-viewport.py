import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt
import dash

app = dash.Dash()


def gen_rows(length):
    return [
        {'a': 'AA', 'b': i} for i in range(length)
    ]


app.layout = html.Div([
    dt.DataTable(rows=gen_rows(5)),
    dt.DataTable(
        rows=gen_rows(10),
        min_height=500
    ),
    dt.DataTable(
        rows=gen_rows(50),
        max_rows_in_viewport=20
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
