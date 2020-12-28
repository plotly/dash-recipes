import dash
import dash_html_components as html
import base64

app = dash.Dash()

encoded_image = base64.b64encode(open('dash_app.png', 'rb').read())

app.layout = html.Div([
    html.Img(src=f'data:image/png;base64,{encoded_image}')
])

if __name__ == '__main__':
    app.run_server(debug=True)
