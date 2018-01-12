import dash
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv')

app = dash.Dash()
app.scripts.config.serve_locally=True
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"})
import json
from textwrap import dedent as d
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import datetime
import pandas as pd

df = pd.read_csv(
    ('https://raw.githubusercontent.com/plotly/'
     'datasets/master/1962_2006_walmart_store_openings.csv'),
    parse_dates=[1, 2],
    infer_datetime_format=True
)
future_indices = df['OPENDATE'] > datetime.datetime(year=2050,month=1,day=1)
df.loc[future_indices, 'OPENDATE'] -= datetime.timedelta(days=365.25*100)


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div([
    html.H1('Walmart Store Openings'),
    html.H3('Dash Histogram Crossfiltering Selections'),
    html.Hr(),
    dcc.RadioItems(
        id='bin',
        options=[{'label': i, 'value': i} for i in [
            'Yearly', 'Seasonally', 'Monthly', 'Weekly'
        ]],
        value='Yearly',
        labelStyle={'display': 'inline'}
    ),
    html.Div([
        html.Div(
            className='six columns',
            children=dcc.Graph(id='openings-over-time')
        ),
        html.Div(
            className='six columns',
            children=dcc.Graph(id='map', animate=True)
        )
    ])
])

@app.callback(
    dash.dependencies.Output('openings-over-time', 'figure'),
    [dash.dependencies.Input('bin', 'value')])
def display_stores_over_time(value):
    return {
        'data': [
            {
                'x': df['OPENDATE'],
                'customdata': df['storenum'],
                'name': 'Open Date',
                'type': 'histogram',
                'autobinx': False,
                'xbins': {
                    'start': '1961-12-31',
                    'end': '2006-12-31',
                    'size': (
                        'M12' if value == 'Yearly' else
                        'M3' if value == 'Seasonally' else
                        'M1' if value == 'Monthly' else
                        1000 * 60 * 60 * 24 * 7   # Weekly
                    )
                }
            }
        ],
        'layout': {
            'margin': {'l': 40, 'r': 20, 't': 0, 'b': 30}
        }
    }


@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('openings-over-time', 'selectedData')])
def display_map(selected_points):
    selected_indices = []
    if selected_points:
        for bin in selected_points['points']:
            selected_indices += bin['pointNumbers']
    return {
        'data': [{
            'lat': df['LAT'],
            'lon': df['LON'],
            'type': 'scattermapbox',
            'selectedpoints': selected_indices,
            'selected': {
                'marker': {'color': '#85144b'}
            }
        }],
        'layout': {
            'mapbox': {
                'center': {
                    'lat': 40,
                    'lon': -100
                },
                'zoom': 2.8,
                'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2oyY2M4YW55MDF1YjMzbzhmemIzb290NiJ9.sT6pncHLXLgytVEj21q43A'
            },
            'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0}
        }
    }

app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
