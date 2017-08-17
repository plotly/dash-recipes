import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash()
app.layout = html.Div([
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=dt(1997, 5, 10)
    ),
    html.Div(id='output')
])

app.scripts.config.serve_locally=True
app.css.config.serve_locally=True

@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('date-picker-single', 'date')])
def display_date(date):
    print(date)
    return 'You have selected {}'.format(date)

if __name__ == '__main__':
    app.run_server(debug=True)
