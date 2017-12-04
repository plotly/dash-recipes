import dash_core_components as dcc
import dash_html_components as html
import dash

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(
        id='latex',
        figure={
            'data': [{'x': [1, 2, 3]}],
            'layout': {'xaxis': {'title': '$\Delta x$'}}
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

