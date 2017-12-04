import dash
from dash.dependencies import Input, Output, Event
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.Button('plot', id='button'),
    html.Div(id='p_section'),


    # html.Div(dcc.Graph(id='hidden-graph', figure={'data': []}), style={'display': 'none'})
])

@app.callback(Output('p_section', 'children'), events=[Event('button', 'click')])
def update_output():
    fig = dcc.Graph(
        id='example',
        figure={
            'data': [{
                'y': [1, 5, 3],
                'type': 'bar'
            }]
        }
    )
    fig2 = dcc.Graph(
        id='example-1',
        figure={
            'data': [{
                'y': [1, 5, 3],
                'type': 'bar'
            }]
        }
    )
    return [fig, fig2]

if __name__ == '__main__':
    app.run_server(debug=True)
