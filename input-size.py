import dash
import dash_core_components as dcc

app = dash.Dash()

app.layout = dcc.Input(style={'width': 30}, type='number', value=5)

if __name__ == '__main__':
    app.run_server(debug=True)

