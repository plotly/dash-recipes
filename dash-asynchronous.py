import dash
from dash.dependencies import Input, Output, Event
import dash_core_components as dcc
import dash_html_components as html

import datetime
import time

class Semaphore:
    def __init__(self, filename='semaphore.txt'):
        self.filename = filename
        with open(self.filename, 'w') as f:
            f.write('done')

    def lock(self):
        with open(self.filename, 'w') as f:
            f.write('working')

    def unlock(self):
        with open(self.filename, 'w') as f:
            f.write('done')

    def is_locked(self):
        return open(self.filename, 'r').read() == 'working'

semaphore = Semaphore()

def long_process():
    if semaphore.is_locked():
        raise Exception('Resource is locked')
    semaphore.lock()
    time.sleep(7)
    semaphore.unlock()
    return datetime.datetime.now()

app = dash.Dash()

def layout():
    return html.Div([
        html.Button('Run Process', id='button'),
        dcc.Interval(id='interval', interval=500),
        dcc.RadioItems(
            id='lock',
            options=[{'label': i, 'value': i} for i in ['Running...', 'Free']]),
        html.Div(id='output')
    ])

app.layout = layout

@app.callback(
    Output('lock', 'value'),
    events=[Event('interval', 'interval')])
def display_status():
    return 'Running...' if semaphore.is_locked() else 'Free'

@app.callback(
    Output('output', 'children'),
    events=[Event('button', 'click')])
def run_process():
    return 'Finished at {}'.format(long_process())

app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True, processes=5)
