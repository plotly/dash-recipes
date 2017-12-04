import dash_core_components as dcc
from datetime import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
from dash.dependencies import Input, Output
import plotly.offline as py

app=dash.Dash()

app.layout=html.Div(children=[
    dcc.DatePickerRange(
        end_date=dt.now(),
        display_format='MMM Do, YY',
        start_date_placeholder_text='MMM Do, YY'
    )
])

if __name__ == '__main__':
    app.run_server()