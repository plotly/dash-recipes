import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.config.supress_callback_exceptions=True

app.layout = html.Div([
    dcc.RadioItems(
        id='toggle-content',
        value='show',
        options=[{'value': i, 'label': i} for i in ['show', 'hide']]
    ),
    html.Div(id='my-content')
])

# Edit your markup here
layout = html.Div([
    html.H1('Dash Test Example!!'),
    dcc.Graph(id='my-graph', figure={'data': [{'x': [1, 2, 3], 'y': [3, 1, 100]}]})
])

# toggle the radio items to refresh content
@app.callback(
    dash.dependencies.Output('my-content', 'children'),
    [dash.dependencies.Input('toggle-content', 'value')])
def display_content(value):
    if value == 'show':
        return layout
    else:
        return html.Div()


if __name__ == '__main__':
    app.run_server(debug=True)
