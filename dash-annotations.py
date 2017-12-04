import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

GDP = {'name': 'GDP_yoy',
 'x': [2012, 2013, 2014, 2015, 2016],
 'y': [103.5, 101.3, 100.7, 97.2, 99.8]}


def make_annotation_item(x, y):
    return dict(xref='x', yref='y',
                x=x, y=y,
                font=dict(color='black'),
                xanchor='left',
                yanchor='middle',
                text='Annotation: {} '.format(y),
                showarrow=False)

ANNOTATIONS = [make_annotation_item(x=GDP['x'][-1], y=GDP['y'][-1])]

app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [GDP],
            'layout': {
                 'xaxis': dict(range=[2010, 2020]),
                 'annotations': ANNOTATIONS
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
