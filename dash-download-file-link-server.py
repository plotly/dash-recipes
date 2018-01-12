import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import flask
import os
import pandas as pd


app = dash.Dash()

app.layout = html.Div([
    html.A(id='download-link', children='Download File'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['NYC', 'LA' 'SF']],
        value='NYC',
        clearable=False
    )
])

@app.callback(Output('download-link', 'href'),
              [Input('dropdown', 'value')])
def update_href(dropdown_value):
    df = pd.DataFrame({dropdown_value: [1, 2, 3]})
    relative_filename = os.path.join(
        'downloads',
        '{}-download.xlsx'.format(dropdown_value)
    )
    absolute_filename = os.path.join(os.getcwd(), relative_filename)
    writer = pd.ExcelWriter(absolute_filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()
    return '/{}'.format(relative_filename)


@app.server.route('/downloads/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(
        os.path.join(root_dir, 'downloads'), path
    )

if __name__ == '__main__':
    app.run_server(debug=True)
