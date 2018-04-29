import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

app = dash.Dash()
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
        dcc.Dropdown(
            id='outer-controls',
            options=[{'label': i, 'value': i} for i in ['a', 'b']],
            value='a'
        ),
        dcc.RadioItems(
            options=[{'label': 'Tab 1', 'value': 1},
                  {'label': 'Tab 2', 'value': 2}],
            value=1,
            id='tabs',
        ),
        html.Div(id='tab-output')
    ])


@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
def display_content(value):
    return html.Div([
        html.Div(id='tab-{}-output'.format(value))
    ])


for tab in ['1', '2']:
    app.callback(
        Output('tab-{}-output'.format(tab), 'children'),
        [Input('outer-controls', 'value')]
    )(lambda value: 'You have selected "{}"'.format(value))




if __name__ == '__main__':
    app.run_server(debug=True)
