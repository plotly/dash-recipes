import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt

import base64
import json
import pandas as pd
import plotly
import io

app = dash.Dash()

app.layout = html.Div([
    html.Div(id='waitfor'),
    dcc.Upload(
        id='upload',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select a File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }
    ),
    html.Div(id='output'),
    html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'})
])

pre_style = {
    'whiteSpace': 'pre-wrap',
    'wordBreak': 'break-all',
    'whiteSpace': 'normal'
}


@app.callback(Output('output', 'children'),
              [Input('upload', 'contents')])
def update_output(contents):
    if contents is not None:
        content_type, content_string = contents.split(',')
        if 'csv' in content_type:
            df = pd.read_csv(io.StringIO(base64.b64decode(content_string).decode('utf-8')))
            return html.Div([
                dt.DataTable(rows=df.to_dict('records')),
                html.Hr(),
                html.Div('Raw Content'),
                html.Pre(contents, style=pre_style)
            ])
        elif 'image' in content_type:
            return html.Div([
                html.Img(src=contents),
                html.Hr(),
                html.Div('Raw Content'),
                html.Pre(contents, style=pre_style)
            ])
        else:
            # xlsx will have 'spreadsheet' in `content_type` but `xls` won't
            # have anything
            try:
                df = pd.read_excel(io.BytesIO(base64.b64decode(content_string)))
                return html.Div([
                    dt.DataTable(rows=df.to_dict('records')),
                    html.Hr(),
                    html.Div('Raw Content'),
                    html.Pre(contents, style=pre_style)
                ])
            except:
                return html.Div([
                    html.Hr(),
                    html.Div('Raw Content'),
                    html.Pre(contents, style=pre_style)
                ])



app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
