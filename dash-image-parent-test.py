import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Header 1'),
    html.H2('Header 2'),
    html.Div(
        children=html.Img(
            src="https://plot.ly/~chris/1639.png",
            style={
                'maxWidth': '100%',
                'maxHeight': '100%',
                'marginLeft': 'auto',
                'marginRight': 'auto'
            }
        ),
        style={
            'width': 400,
            'height': 200,
            'border': 'thin grey solid'
        }
    )
])

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=True)
