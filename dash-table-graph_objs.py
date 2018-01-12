import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

app = dash.Dash(__name__)
server=app.server
#server.secret_key = os.environ.get('secret_key', 'secret')

trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))

data = [trace]
app.layout = html.Div([
    #dcc.Graph( id = "heatmap", figure = go.Figure( data = [go.Heatmap(z=[[1, 20, 30], [20, 1, 60], [30, 60, 1]])] ) ),
    dcc.Graph(id='visitors1',figure = go.Figure(data=[trace]))
])

if __name__ == '__main__':
    app.run_server(debug=True)
