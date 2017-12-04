import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/dZVMbK.css'})

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

y_data = 'lifeExp'
x_data = 'gdpPercap'

app.layout = html.Div(className="row", children=[

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            figure={
                'data': [{
                    'x': df[df['year'] == 2007][x_data],
                    'y': df[df['year'] == 2007][y_data],
                    'customdata': df[df['year'] == 2007]['country'],
                    'mode': 'markers',
                    'marker': {
                        'size': 12,
                        'color': 'rgba(0, 116, 217, 0.5)',
                        'line': {
                            'color': 'rgb(0, 116, 217)',
                            'width': 0.5
                        }
                    }
                }],
                'layout': {
                    'xaxis': {
                        'title': x_data,
                    },
                    'yaxis': {
                        'title': y_data,
                    },
                    'margin': {
                        'l': 50,
                        'r': 10,
                        't': 10,
                        'b': 50
                    },
                    'hovermode': 'closest'
                }
            },
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ], className="six columns"),

    html.Div([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], className="six columns")

])


def create_time_series(dff, column, title):
    return {
        'data': [go.Scatter(
            x=dff['year'],
            y=dff[column],
            mode='lines+markers',
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 50, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {'type': 'linear', 'title': column},
            'xaxis': {'showgrid': False}
        }
    }


@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData')])
def update_y_timeseries(hoverData):
    country_name = hoverData['points'][0]['customdata']
    dff = df[df['country'] == country_name]
    title = '<b>{}</b>'.format(country_name)
    return create_time_series(dff, y_data, title)


@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData')])
def update_x_timeseries(hoverData):
    country_name = hoverData['points'][0]['customdata']
    dff = df[df['country'] == country_name]
    title = '<b>{}</b>'.format(country_name)
    return create_time_series(dff, x_data, title)


if __name__ == '__main__':
    app.run_server(debug=True, port=8070)
