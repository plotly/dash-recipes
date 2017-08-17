import dash_core_components as dcc
import dash_html_components as html
import dash

app = dash.Dash()

app.layout = html.Div([
    dcc.Link('Unstyled Link', href="/page-1"),
    dcc.Link('Styled Link', href="/page-2", style={"color": "red", "text-decoration": "none"})
])


if __name__ == '__main__':
    app.run_server(debug=True)
