# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

all_options = {
    'America': {
        'New York': ['Statue of Liberty', 'Empire State Building'],
        'San Francisco': ['Golden Gate Bridge', 'Mission District'],
    },
    'Canada': {
        u'Montréal': ['Biodome', 'Parc Laurier'],
        'Toronto': ['CN Tower', 'Royal Ontario Museum'],
    }
}
app.layout = html.Div([
    dcc.RadioItems(
        id='countries-dropdown',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='America'
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-dropdown'),

    html.Hr(),

    dcc.RadioItems(id='landmarks-dropdown'),

    html.Div(id='display-selected-values')

])


@app.callback(
    dash.dependencies.Output('cities-dropdown', 'options'),
    [dash.dependencies.Input('countries-dropdown', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    dash.dependencies.Output('cities-dropdown', 'value'),
    [dash.dependencies.Input('cities-dropdown', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    dash.dependencies.Output('landmarks-dropdown', 'options'),
    [dash.dependencies.Input('countries-dropdown', 'value'),
     dash.dependencies.Input('cities-dropdown', 'value')])
def set_landmarks_options(selected_country, selected_city):
    return [{'label': i, 'value': i} for i in all_options[selected_country][selected_city]]


@app.callback(
    dash.dependencies.Output('landmarks-dropdown', 'value'),
    [dash.dependencies.Input('landmarks-dropdown', 'options')])
def set_landmarks_value(available_options):
    return available_options[0]['value']


@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('countries-dropdown', 'value'),
     dash.dependencies.Input('cities-dropdown', 'value'),
     dash.dependencies.Input('landmarks-dropdown', 'value')])
def set_display_children(selected_country, selected_city, selected_landmark):
    return u'{} is in {}, {}'.format(
        selected_landmark, selected_city, selected_country,
    )

if __name__ == '__main__':
    app.run_server(debug=True)
