import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div([
    html.Div('Data-*', **{'data-test': 'lah lah'}),
    html.Div('Aria-*', **{'aria-test': 'lah lah loo'})
])

if __name__ == '__main__':
    app.run_server(debug=True)
