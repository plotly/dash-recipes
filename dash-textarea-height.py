import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    html.Div([
        html.Div([
            dcc.Textarea(
                id='input_query',
                placeholder='Enter/Review Query...',
                rows=50,
                style={'width': '100%'}
            ),
        ]),
    ])
)


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
