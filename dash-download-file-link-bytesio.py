# Adapted from https://community.plotly.com/t/allowing-users-to-download-csv-on-click/5550/19
# example sends Excel .xlsx file type, for other mimetypes, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import flask
import io

import pandas as pd

df = pd.DataFrame({
    'Gender': ['m', 'f', 'o', 'm'],
    'JoinDate': ['19970309', '14200420', '19870930', '03421206'],
    'ZipState': ['x', 'x', 'y', 'y']
})

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.layout = html.Div([

    html.Label('Filter gender'),
    dcc.Input(id='gender-picker', value='m', type='text'),

    html.Label('Filter join date'),
    dcc.Input(id='joindate', value='14200420', type='text'),

    html.Label('Filter state'),
    dcc.Input(id='state-picker', value='x', type='text'),

    html.A(html.Button('Download', id='download-button'), id='download-link')
    ])

@app.callback(
    dash.dependencies.Output('download-link', 'href'),
    [dash.dependencies.Input('gender-picker', 'value'),
     dash.dependencies.Input('joindate', 'value'),
     dash.dependencies.Input('state-picker', 'value')])
def update_link(selected_gender, join_start_date, selected_state):
    return '/DownloadData?value={}/{}/{}'.format('-'.join(selected_gender),
                                                                  dt.strptime(join_start_date,'%Y%m%d'),
                                                                  '-'.join(selected_state))

@app.server.route('/DownloadData')
def download_csv():
    # get parsing details from url that was just updated
    value = flask.request.args.get('value')
    value = value.split('/')
    
    selected_gender = value[0].split('-')
    selected_state = value[2].split('-')
    join_start_date = value[1]
    
    filtered_df = df[df['Gender'].isin(selected_gender)]
    filtered_df = filtered_df[filtered_df['ZipState'].isin(selected_state)]
    filtered_df = filtered_df.loc[(demographics['JoinDate'] >= join_start_date),]
    
    str_io = io.BytesIO()
    filtered_df.to_excel(str_io)

    mem = io.BytesIO()
    mem.write(str_io.getvalue()
    mem.seek(0)
    str_io.close()
    return flask.send_file(mem,
                       mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                       attachment_filename='downloadFile.xlsx',
                       as_attachment=True)

if __name__ == '__main__':
    app.run_server()