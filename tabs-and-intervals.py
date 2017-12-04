import dash
from dash.dependencies import Input, Output, Event, State
import dash_core_components as dcc
import dash_html_components as html

import datetime

app = dash.Dash()
app.scripts.config.serve_locally = True
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    dcc.Tabs(
        tabs=[
            {'label': 'Tab {}'.format(i), 'value': i} for i in range(1, 5)
        ],
        value=3,
        id='tab'
    ),
    html.Div(id='container'),
    dcc.Interval(id='my-interval', interval=3*1000)
])


def generate_figure(selected_tab):
    now = datetime.datetime.now()
    return {
        'data': [{'y': [1, 5, 3]}],
        'layout': {
            'title': 'Tab {} at {}:{}:{}'.format(
                selected_tab, now.hour, now.minute, now.second
            )
        }
    }


@app.callback(Output('container', 'children'), [Input('tab', 'value')])
def display_content(selected_tab):
    return html.Div([
          html.H1(selected_tab),
          dcc.Graph(id='graph', figure=generate_figure(selected_tab))
    ])


app.callback(
    Output('graph', 'figure'),
    events=[Event('my-interval', 'interval')],
    state=[State('tab', 'value')])(generate_figure)


if __name__ == '__main__':
    app.run_server(debug=True)
