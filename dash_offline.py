import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash('offline example')

app.layout = html.Div([
    dcc.Graph(id='my-graph', figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 1]}]})
])

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True)
