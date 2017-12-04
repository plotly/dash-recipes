import dash
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')

app = dash.Dash()
app.scripts.config.serve_locally=True
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"})


app.layout = html.Div([
    html.H1('Dash App'),
    html.Div(id='text-element'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': i, 'value': i}
            for i in df.YEAR.unique()
        ],
        value=2001
    ),
    dcc.Graph(
        id='my-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar'}
            ]
        }
    )
])

@app.callback(
    dash.dependencies.Output('text-element', 'children'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_text(new_year):
    dff = df[df.YEAR == new_year]
    return 'There were {} stores in {}'.format(
        len(dff),
        new_year
    )

@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_graph(new_value):
    dff = df[df.YEAR == new_value]
    return {
        'data': [{
            'lat': dff.LAT,
            'lon': dff.LON,
            'type': 'scattermapbox',
        }],
        'layout': {'mapbox': {'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2oyY2M4YW55MDF1YjMzbzhmemIzb290NiJ9.sT6pncHLXLgytVEj21q43A'}}
    }

if __name__ == '__main__':
    app.run_server(debug=True)
