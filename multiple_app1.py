import dash
import dash_html_components as html

from multiple_server import server

app1 = dash.Dash(name='app1', server=server, url_base_pathname='/app1/')
app1.layout = html.H1('App 1')
print('app1 {}'.format(app1.config.requests_pathname_prefix))
print('app1 {}'.format(app1.url_base_pathname))
