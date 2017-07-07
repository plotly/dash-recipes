import dash
from dash.dependencies import Event, Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# Edit this object!
layout = html.Div([
    html.H1('Hello Dash!'),
    html.H3('Dash with live-reload'),
])

# Barebones layout
app.layout = html.Div([
    dcc.Interval(id='refresh', interval=200),
    html.Div(id='content', className="container")
])

# Update the `content` div with the `layout` object.
# When you save this file, `debug=True` will re-run
# this script, serving the new layout
@app.callback(
    Output('content', 'children'),
    events=[Event('refresh', 'interval')])
def display_layout():
    return layout

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
