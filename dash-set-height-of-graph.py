import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

stats= {
    'Goals': [43,32,19,32,20,15,20,19,19,21,19,8,14],
    'Assists': [67, 55, 63, 39, 36, 34, 23, 21, 20, 16, 15, 26, 17],
    'Points' : [110, 86, 82, 71, 56, 49, 43, 40, 39, 37, 34, 34, 31],
    'Shots' : [223, 202, 167, 172, 147, 115, 135, 103, 119, 112, 120, 101, 102]
    }
df = pd.DataFrame(stats)

#button options
options = [{'label': str(i), 'value':str(i)} for i in ['Goals','Assists','Points','Shots']]

#grid layout
container= {
    'display':'grid',
    'grid-template-columns':'repeat(2, 1fr)',
    'grid-template-rows':'repeat(2, minmax(100px, auto))',
    'grid-padding': '1em',
}

#placeholder layout
placeholder = {
    'background': "#eee",
    'border-style':'solid',
    'border-size':'0.5em',
    'border-color':'#ddd'
}

app = dash.Dash('')
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div([
    # grid 1,1
    html.Div([
        html.Div(
                dcc.Dropdown(
                    id='category',
                    options= options,
                    value= 'Goals'
                    ),
                ),
        html.Div([
                dcc.Graph(
                    id='histogram',
                    style={'height':'80vh', 'width':'55vw'}
                )
        ]),
        # grid 1,2
        html.Div('placeholder', style=placeholder)
        ]),
    #grid 2,1
    html.Div([
        html.Div([
                #feature dropdown
                dcc.Dropdown(
                    id='xvalue',
                    options=options,
                    value ='goals'
                    ),
                dcc.Dropdown(
                    id='yvalue',
                    options=options,
                    value='goals'
                    ),
                ]),
        html.Div(
            dcc.Graph( id ='scatter' ,  style={'height':'80vh', 'width':'55vw'})
            )
        ]),
    #grid 2,2
    html.Div(
        'placeholder',  style=placeholder )
    ], style=container )

#histogram callback
@app.callback(
    dash.dependencies.Output('histogram', 'figure'),
    [dash.dependencies.Input('category', 'value')]
)
def update_histogram(value):
    return {
        'data':[
           go.Histogram(
            x=df[value]
            )],
        'layout':go.Layout()
            }


@app.callback(
    dash.dependencies.Output('scatter', 'figure'),
    [dash.dependencies.Input('xvalue', 'value'),
    dash.dependencies.Input('yvalue', 'value')]
)
def update_scatter(xvalue,yvalue):
    return {
        'data': [
             go.Scatter(
                x=df[xvalue],
                y=df[yvalue],
                mode='markers'
            )
         ] ,
    'layout' : go.Layout( )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
