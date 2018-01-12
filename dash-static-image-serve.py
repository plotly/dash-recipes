import dash
import dash_html_components as html
import os

import config

STATIC_PREFIX = '/{}/static/'.format(config.DASH_APP_NAME)

app = dash.Dash()

app.layout = html.Div([
    html.Img(src='{}my-image.png'.format(STATIC_PREFIX))
])


# Static routes for on-premise are a little bit different than local
# because the Plotly On-Premise proxy server strips away the app name
# before forwarding the request to Dash

if 'DYNO' in os.environ:
    static_route = '/static/<path:path>'
else:
    static_route = '/{}/static/<path:path>'.format(config.DASH_APP_NAME)

@server.route(static_route)
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(
        os.path.join(root_dir, 'static'), path
)
