import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash('input-disabled')
app.layout = html.Div(
    [
        dcc.Input(
            disabled='disabled',
            type='text',
            value='test me'
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
