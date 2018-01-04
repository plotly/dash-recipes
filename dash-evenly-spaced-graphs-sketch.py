def EvenlySpacedGraphs(figures):
    return html.Div([
        dcc.Graph(figure=figure, style={
            'width': 'calc(100% / {})'.format(len(figures))
        }, id='graph-{}'.format(i))
        for (i, figure) in enumerate(figures)
    ], className='row')


app.layout = html.Div([
    html.Div(id='div-container')
])

@app.callback(Output('div-container', 'children'), [...])
def update_graphs(...):
    figures = ... # your own function that generates the figures
    return EvenlySpacedGraphs(figures)
