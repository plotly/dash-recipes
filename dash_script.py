import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Script('alert(1);', type='text/javascript')
])

if __name__ == '__main__':
    app.run_server()
