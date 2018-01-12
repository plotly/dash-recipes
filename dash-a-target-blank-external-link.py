import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.A("Link to external site", href='https://plot.ly', target="_blank")
])

if __name__ == '__main__':
    app.run_server(debug=True)
