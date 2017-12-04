import dash
import dash_html_components as html
import dash_core_components as dcc
from flask import send_from_directory
import os

app = dash.Dash()

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/static/stylesheet.css'
    ),
    html.Div('Assets loading locally')
])


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


if __name__ == '__main__':
    app.run_server(debug=True)
