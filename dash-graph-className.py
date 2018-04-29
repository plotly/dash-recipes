import dash
import dash_core_components as dcc

app = dash.Dash()

app.layout = dcc.Graph(
    id='graph',
    className='my-class',
    figure={'data': [{'x': [1, 2, 3]}]}
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8089)
