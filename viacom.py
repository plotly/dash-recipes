import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': ['A', 'B', 'A', 'B']
})

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': i, 'value': i} for i in df['b'].unique()
        ],
        value='A'
    ),
    html.Div(id='my-output')
])

@app.callback(
    dash.dependencies.Output('my-output', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def display_value(value):
    dff = df[df['b'] == value]
    return list(dff)

if __name__ == '__main__':
    app.run_server(debug=True)
