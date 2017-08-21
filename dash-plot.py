# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import datetime
from datetime import timedelta

app = dash.Dash()


x_data = ['DSL', 'Gas', 'Electricty']

start = go.Bar(
    x=[datetime.datetime(y, m, d) for (y, m, d) in [(2015, 10, 1), (2015, 10, 2), (2015, 10, 3)]],
    y=x_data,
    marker=dict(
        color='rgba(1,1,1, 0.0)',
    )
)

end = go.Bar(
    x=[datetime.datetime(y, m, d) for (y, m, d) in [(2015, 12, 1), (2015, 12, 2), (2015, 12, 3)]],
    y=x_data,
    marker=dict(
        color='rgba(55, 128, 191, 0.7)',
        line=dict(
            color='rgba(55, 128, 191, 1.0)',
            width=2,
        )
    )
)


x_data1 = ['DSL1', 'Gas1', 'Electricty1']

start1 = go.Bar(
    x=[20, 40, 60],
    y=x_data1,
    marker=dict(
        color='rgba(1,1,1, 0.0)',
    )
)

end1 = go.Bar(
    x=[100, 200, 300],
    y=x_data1,
    marker=dict(
        color='rgba(55, 128, 191, 0.7)',
        line=dict(
            color='rgba(55, 128, 191, 1.0)',
            width=2,
        )
    )
)





def build_data(contract_name, stream): # one stream only
	data = []
	#t0 = datetime.datetime.now() + datetime.timedelta(year=-1)
	month_list = sorted([z['month'] for z in stream['monthList']])
	month_list = [datetime.datetime.strptime(month, '%Y-%m-%d') for month in month_list]
	print(month_list)

	min_month = min(month_list)
	max_month = max(month_list)

	#month_list = [(month - min_month).days for month in month_list]

	#min_month = min(month_list)
	#max_month = max(month_list)


	length = len(month_list)


	print("////////////////////")
	print(month_list)
	print((min_month, "===", max_month))
	print("////////////////////")

	#for i in range(0, length-1):
	#start = month_list[i]
	#end = month_list[i+1]

	start = go.Bar(y=[min_month, min_month + datetime.timedelta(days=1)], x=[contract_name, 'x'], orientation='h', marker=dict(color='rgba(1,1,1, 0.0)'))
	end = go.Bar(y=[max_month, max_month + datetime.timedelta(days=1)], x=[contract_name, 'y'], orientation='h', marker=dict(color='rgba(55, 128, 191, 0.7)',
		line=dict( color='rgba(55, 128, 191, 1.0)', width=2,)))
	data.append(start)
	data.append(end)
	return data


def plot_bar(data):
	app.layout = html.Div(children=[html.H1(children='CM PT'), html.Div(children='''History.'''),

	dcc.Graph(
		figure=go.Figure(
		data = data,
		layout=go.Layout(title='Streams', showlegend=False, barmode='stack', margin=go.Margin(l=200, r=0, t=40, b=20))),
	style={'height': 300},
	id='my-graph')
	])





example_stream={'status': 'active', 'numberOfTransactions': 2, 'bookingTypes': [''], 'amountPerMonth': 3987.5, 'coeffOfVariation': 0.0, 'firstPayment': '2017-04-27', 'confidence': 1.0, 'groupKey': '', 'accountTypes': ['Giro account'], 'transactionsPerMonth': 1.0, 'monthList': [{'transactions': [{'partnerName': '', 'uid': 99999999, 'amount': 3987.5, 'bookingType': '', 'subclf': '1_1', 'bookingDate': '27-04-2017', 'partnerAccountIBAN': ''}], 'month': '2017-04-01'}, {'transactions': [{'partnerName': '', 'uid': 111.0, 'amount': 3987.5, 'bookingType': '', 'subclf': '1_1', 'bookingDate': '29-05-2017', 'partnerAccountIBAN': ''}], 'month': '2017-05-01'}], 'partnerName': '', 'highestAmount': 3987.5, 'numberOfTransactionPerMonthWithTransaction': 1.0, 'overallAvailableMonths': 2, 'windowSize': '1M', 'lastPayment': '2017-05-29', 'nrMonthsWithTransaction': 2, 'numberOfMonths': 2, 'groupKeyType': 'partnerName', 'lowestAmount': 3987.5, 'nrMonthsWithoutTransaction': 0, 'amount': 3987.5, 'meanAmount': 3987.5, 'medianAmount': 3987.5, 'subclasses': ['1_1', '1_2'], 'missedMonthsSinceLatestTransaction': 0}



if __name__ == '__main__':
	data = build_data('S', example_stream)
	plot_bar(data)
	print(data)
	app.run_server(debug=True)
