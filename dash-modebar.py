import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(
	id='my-graph',
	figure={
		'data': [{'x': [1, 2, 3]}]
	},
	config={
	      'modeBarButtonsToRemove': [
        	'sendDataToCloud',
	        'pan2d',
        	'zoomIn2d',
	        'zoomOut2d',
	        'autoScale2d',
	        'resetScale2d',
	        'hoverCompareCartesian',
	        'hoverClosestCartesian',        
	        'toggleSpikelines'        
	      ],
		'displayModeBar': True,
		'displaylogo': False
	}
    )
])

if __name__ == '__main__':
	app.run_server(debug=True)
