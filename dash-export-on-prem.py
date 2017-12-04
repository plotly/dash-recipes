import dash
import dash_html_components as html
import dash_core_components as dcc
from flask import send_from_directory
import os

app = dash.Dash()


app.scripts.append_script({
    'external_url': '/static/on-prem.js'
})

app.layout = html.Div([
    dcc.Graph(
        id='my-graph',
        figure={
            'data': [{
                'x': [1, 2, 3],
                'y': [4, 1, 2]
            }],
        }
])


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)


if __name__ == '__main__':
    app.run_server(debug=True)
