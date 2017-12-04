import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import itertools

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='datasource-1',
        options=[
            {'label': i, 'value': i} for i in ['A', 'B', 'C']
        ],
    ),
    dcc.Dropdown(
        id='datasource-2',
        options=[
            {'label': i, 'value': i} for i in ['X', 'Y', 'Z']
        ]
    ),
    html.Hr(),
    html.Div('Dynamic Controls'),
    html.Div(
        id='controls-container'
    ),
    html.Hr(),
    html.Div('Output'),
    html.Div(
        id='output-container'
    )
])

def generate_control_id(value):
    return 'Control {}'.format(value)

DYNAMIC_CONTROLS = {
    'A': dcc.Dropdown(
        id=generate_control_id('A'),
        options=[{'label': 'Dropdown A: {}'.format(i), 'value': i} for i in ['A', 'B', 'C']]
    ),
    'B': dcc.Dropdown(
        id=generate_control_id('B'),
        options=[{'label': 'Dropdown B: {}'.format(i), 'value': i} for i in ['A', 'B', 'C']]
    ),
    'C': dcc.Dropdown(
        id=generate_control_id('C'),
        options=[{'label': 'Dropdown C: {}'.format(i), 'value': i} for i in ['A', 'B', 'C']]
    ),

    'X': dcc.Dropdown(
        id=generate_control_id('X'),
        options=[{'label': 'Dropdown X: {}'.format(i), 'value': i} for i in ['A', 'B', 'C']]
    ),
    'Y': dcc.Dropdown(
        id=generate_control_id('Y'),
        options=[{'label': 'Dropdown Y: {}'.format(i), 'value': i} for i in ['A', 'B', 'C']]
    ),
    'Z': dcc.Dropdown(
        id=generate_control_id('Z'),
        options=[{'label': 'Dropdown Z: {}'.format(i), 'value': i} for i in ['A', 'B', 'C']]
    )
}

@app.callback(
    Output('controls-container', 'children'),
    [Input('datasource-1', 'value'),
     Input('datasource-2', 'value')])
def display_controls(datasource_1_value, datasource_2_value):
    # generate 2 dynamic controls based off of the datasource selections
    return html.Div([
        DYNAMIC_CONTROLS[datasource_1_value],
        DYNAMIC_CONTROLS[datasource_2_value],
    ])

def generate_output_id(value1, value2):
    return '{} {} container'.format(value1, value2)

@app.callback(
    Output('output-container', 'children'),
    [Input('datasource-1', 'value'),
     Input('datasource-2', 'value')])
def display_controls(datasource_1_value, datasource_2_value):
    # create a unique output container for each pair of dyanmic controls
    return html.Div(id=generate_output_id(
        datasource_1_value,
        datasource_2_value
    ))

def generate_output_callback(datasource_1_value, datasource_2_value):
    def output_callback(control_1_value, control_2_value):
        # This function can display different outputs depending on
        # the values of the dynamic controls
        return '''
            You have selected {} and {} which were
            generated from {} (datasource 1) and and {} (datasource 2)
        '''.format(
            control_1_value,
            control_2_value,
            datasource_1_value,
            datasource_2_value
        )
    return output_callback

app.config.supress_callback_exceptions = True

# create a callback for all possible combinations of dynamic controls
# each unique dynamic control pairing is linked to a dynamic output component
for value1, value2 in itertools.product(
        [o['value'] for o in app.layout['datasource-1'].options],
        [o['value'] for o in app.layout['datasource-2'].options]):
    app.callback(
        Output(generate_output_id(value1, value2), 'children'),
        [Input(generate_control_id(value1), 'value'),
         Input(generate_control_id(value2), 'value')])(
        generate_output_callback(value1, value2)
    )

if __name__ == '__main__':
    app.run_server(debug=True)
