import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
from dash.dependencies import Input, Output, State, Event

app = dash.Dash(__name__)

app.config['suppress_callback_exceptions'] = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

server = app.server

app.layout = html.Div([
    dcc.Input(id='end_time',
              value='2017-09-14',
              type='text',
              style={'width': '300'}),
    html.Div(children=None, id='date-container'),
    dcc.DatePickerSingle(id='single'),
    html.Div(id='date-container-output'),
])


@app.callback(
    Output('date-container', 'children'),
    [Input('end_time', 'value')])
def change(end_date):
    end = dt.datetime.strptime(end_date, '%Y-%m-%d')
    start = end - dt.timedelta(days=3)
    date_picker = dcc.DatePickerRange(
        id='date_picker_range',
        start_date=start,
        end_date=end,
        max_date_allowed=end
    )
    return date_picker


@app.callback(
    Output('single', 'date'),
    [Input('end_time', 'value')])
def change(datestring):
    return dt.datetime.strptime(datestring, '%Y-%m-%d')


@app.callback(
    Output('date-container-output', 'children'),
    [Input('date_picker_range', 'start_date'),
     Input('date_picker_range', 'end_date'),
     Input('single', 'date')])
def display_dates(start, end, single):
    return 'You have selected "{}"-"{}" and "{}"'.format(start, end, single)


if __name__ == '__main__':
    app.run_server(debug=True)
