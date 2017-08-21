import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()


tab_style = {
    'color': '#0074D9',
    'text-decoration': 'underline',
    'margin': 30,
    'cursor': 'pointer'
}

app.layout = html.Div([
    dcc.Location(id='url'),
    dcc.Link('Tab 1', href='/', style=tab_style),
    dcc.Link('Tab 2', href='/tab-2', style=tab_style),
    dcc.Link('Tab 3', href='/tab-3', style=tab_style),
    html.Div([

        # Tab 1
        html.Div(
            id='tab-1',
            style={'display': 'none'},
            children=[
                html.H1('Tab 1'),
                dcc.Dropdown(
                    id='dropdown-1',
                    options=[
                        {'label': 'Tab 1: {}'.format(i), 'value': i}
                        for i in ['A', 'B', 'C']
                    ]
                ),
                html.Div(id='display-1')
            ]
        ),

        # Tab 2
        html.Div(
            id='tab-2',
            style={'display': 'none'},
            children=[
                html.H1('Tab 2'),
                dcc.Dropdown(
                    id='dropdown-2',
                    options=[
                        {'label': 'Tab 2: {}'.format(i), 'value': i}
                        for i in ['A', 'B', 'C']
                    ]
                ),
                html.Div(id='display-2')
            ]
        ),

        # Tab 3
        html.Div(
            id='tab-3',
            style={'display': 'none'},
            children=[
                html.H1('Tab 3'),
                dcc.Dropdown(
                    id='dropdown-3',
                    options=[
                        {'label': 'Tab 3: {}'.format(i), 'value': i}
                        for i in ['A', 'B', 'C']
                    ]
                ),
                html.Div(id='display-3')
            ]
        ),
    ])
])


def generate_display_tab(tab):
    def display_tab(pathname):
        if tab == 'tab-1' and (pathname is None or pathname == '/'):
            return {'display': 'block'}
        elif pathname == '/{}'.format(tab):
            return {'display': 'block'}
        else:
            return {'display': 'none'}
    return display_tab


for tab in ['tab-1', 'tab-2', 'tab-3']:
    app.callback(Output(tab, 'style'), [Input('url', 'pathname')])(
        generate_display_tab(tab)
    )


@app.callback(
    Output('display-1', 'children'),
    [Input('dropdown-1', 'value')])
def display_value(value):
    return 'You have selected {}'.format(value)


@app.callback(
    Output('display-2', 'children'),
    [Input('dropdown-2', 'value')])
def display_value(value):
    return 'You have selected {}'.format(value)


@app.callback(
    Output('display-3', 'children'),
    [Input('dropdown-3', 'value')])
def display_value(value):
    return 'You have selected {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
