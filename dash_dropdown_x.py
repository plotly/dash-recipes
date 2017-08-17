import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

app = dash.Dash()
app.layout = html.Div([
    html.H1(children='Dropdown test'),
    dcc.Dropdown(
                id='test-selector',
                placeholder='Select a value',
                options=[{'label':'foo', 'value':0},{'label':'bar', 'value':1},{'label':'baz', 'value':2}],
                multi=True
    ),
    html.Div(
        id='foobar'
    )

])

@app.callback(
    Output(component_id='foobar', component_property='children'),
    [Input(component_id='test-selector', component_property='value')]
)
def test_interaction(value):
    print(value)
    return value

app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True)
