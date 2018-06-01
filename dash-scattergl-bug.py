# Investigating https://github.com/plotly/plotly.js/issues/2609#issuecomment-386302768

import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly import tools
import plotly.graph_objs as go


app = dash.Dash()


fig = tools.make_subplots(3, 1, shared_xaxes=True)
fig.append_trace(go.Scattergl({
      'x': df_1.index,
      'y': df1['column'].values,
      'mode': 'lines',
      'name': 'df1',
}), 1, 1)
  fig.append_trace(go.Scattergl({
      'x': df2.index,
      'y': df2['column'].values,
      'mode': 'lines',
      'name': 'df2',
  }), 2, 1)
  fig.append_trace(go.Scattergl({
      'x': df3.index,
      'y': df3['column'].values,
      'mode': 'lines',
      'name': 'df3',
  }), 3, 1)
fig['layout'].update(height=1200, title=children)
return fig

app.layout = html.Div([
    dcc.Graph(id='scattergl', figure={
        'data': [
            {
                'x'
            }
        ]
    })
])
