import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html



app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})



app.layout = html.Div(
			children = [
				html.Div(
				id = 'list',
				children = [ dcc.Checklist(id = "myList")]),
			html.Button('Fill Checklist', id='list-btn', n_clicks=0)]
			)


@app.callback(
	Output('myList', 'options'),
	[Input('list-btn', 'n_clicks')]
	)
def fillChecklist(n_clicks):
    data = [['label-1', '1'],['label-2', '2']]
    return [{'label': x[0] +" "+ x[1], 'value' : x[1] } for x in data]

if __name__ == '__main__':
    app.run_server(debug=True)
