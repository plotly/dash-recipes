import dash, dash_core_components as dcc, dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()
app.layout = html.Div([
        dcc.Graph(id='a', figure=dict(data = [go.Scatter( x = [1,2], y = [3,4] )])),
        dcc.Graph(id='b', figure=dict(data = [go.Scatter( x = [1,2], y = [3,4] )])),
        ], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)
