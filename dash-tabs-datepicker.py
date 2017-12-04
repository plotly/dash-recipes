import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dtime

app = dash.Dash()


app.config['suppress_callback_exceptions'] = True
app.layout = html.Div([
    dcc.DatePickerRange(
        id='Dr1',
        clearable=True,
        reopen_calendar_on_clear=True,
        start_date_placeholder_text='Select a date',
        end_date=dtime.today().strftime("%Y-%m-%d")
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    [Input('Dr1', 'start_date'),
     Input('Dr1', 'end_date')])
def dates_selected(start_date, end_date):
    value = "From- %s  To-   %s" % (start_date, end_date)
    return value


if __name__ == '__main__':
    app.run_server(debug=True)
