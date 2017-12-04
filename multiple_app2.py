import dash
import dash_html_components as html

from multiple_server import server

app2 = dash.Dash(name='app2', server=server, url_base_pathname='/app2/')
app2.layout = html.H1('App 2')
print('app2 {}'.format(app2.config.requests_pathname_prefix))
print('app2 {}'.format(app2.url_base_pathname))
