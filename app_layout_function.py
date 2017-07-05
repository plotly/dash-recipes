import dash
import dash_html_components as html

app = dash.Dash()

def serve_layout():
    print('serve layout')
    return html.Div('hlo world')

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=False)
