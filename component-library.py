# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import json

app = dash.Dash()

def layout(id):
    return html.Div([
        html.Label('Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL',
            id='{}-dropdown'.format(id)
        ),

        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF'],
            multi=True,
            id='{}-multi-dropdown'.format(id)
        ),

        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL',
            id='{}-radio-items'.format(id)
        ),

        html.Label('Checkboxes'),
        dcc.Checklist(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            values=['MTL', 'SF'],
            id='{}-checkboxes'.format(id)
        ),

        html.Label('Text Input'),
        dcc.Input(
            value='MTL',
            type='text',
            id='{}-input'.format(id)
        ),

        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=5,
            id='{}-slider'.format(id)
        ),

        html.Label('Range Slider'),
        dcc.RangeSlider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=[5, 8],
            id='{}-range-slider'.format(id)
        ),

        html.Label('Slider on Drag'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=5,
            updatemode='drag',
            id='{}-slider-drag'.format(id)
        ),

        html.Label('Range Slider'),
        dcc.RangeSlider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=[5, 8],
            updatemode='drag',
            id='{}-range-slider-drag'.format(id)
        )

    ])


app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.H3('Uncontrolled Components'),
    layout('xx'),
    html.Hr(),
    html.H3('Controlled Components'),
    layout('controlled'),
    html.Div(id='output-value')
])

INPUTS = [
    Input(id_, 'value') for id_ in list(app.layout.keys())
    if 'controlled' in id_ and 'checkboxes' not in id_]
INPUTS.append(Input('controlled-checkboxes', 'values'))


@app.callback(
    Output('output-value', 'children'),
    INPUTS)
def display_values(*args):
    return json.dumps(args)


if __name__ == '__main__':
    app.run_server(debug=True)
