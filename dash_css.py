import dash
import dash_core_components as dcc
import dash_html_components as html

import flask
import os

appname = 'testapp'

app = dash.Dash(__name__)
app.config.requests_pathname_prefix = '/{}/'.format(
    appname
)


app.layout = html.Div('Hello World')

stylesheet = 'stylesheet.css'


@app.server.route('/{}/{}'.format(appname, stylesheet))
def serve_stylesheet():
    return flask.send_from_directory(os.getcwd(), stylesheet)


app.css.append_css({"external_url": "/static/{}".format(stylesheet)})

if __name__ == '__main__':
    app.run_server(debug=True)
