import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd

app = dash.Dash()

app.scripts.config.serve_locally=True

df_simple = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': [1, 19, 10]
})

df_complex = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')

app.layout = html.Div([
    dt.EditableTable(
        id='editable-table',
        editable=True,
        dataframe=df_simple.to_dict()
    ),

    dcc.Graph(id='my-graph', animate=True),

    html.Div(
        dt.EditableTable(dataframe=df_complex.iloc[0:50].to_dict()),
        style={'height': 100, 'overflow-y': 'scroll'}
    )

])


@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('editable-table', 'dataframe')])
def update_graph(dataframe_dict):
    df = pd.DataFrame(dataframe_dict)
    return {
        'data': [{
            'x': df['Column 1'],
            'y': df['Column 2']
        }]
    }

app.css.append_css({"external_url": [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    "https://codepen.io/chriddyp/pen/rzyyWo.css"
]})

if __name__ == '__main__':
    app.run_server(debug=True)
