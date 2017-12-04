import numpy as np
import pandas as pd
from itertools import product
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt
from dash.dependencies import Input, Output
import plotly.graph_objs as go

np.random.seed(13)

# ------------------------------------------------------------------------------------------------
# data generator
# multidimensional time series data
def base_signal(length, qty_start, qty_end, noise):
    """simple signal with trend and noise"""
    x = np.linspace(qty_start, qty_end, length)
    return x * np.random.normal(loc=1, scale=noise, size=length)


def seasonality(length, period, phase, amplitude):
    """multiplicative seasonal coefficient"""
    x = np.linspace(0, length * 2 * np.pi / period, length)
    x += phase * 2 * np.pi
    return 1 + amplitude * np.sin(x)

n_weeks = 52

# products
n_products = 20
df_product = pd.DataFrame({
    'product_id': range(n_products),
    'product_name': ['product %d' % i for i in range(n_products)],
    'qty_start': np.random.uniform(50, 150, n_products),
    'qty_end': np.random.uniform(50, 150, n_products),
    'noise': np.random.uniform(0, 0.2, n_products)
    }).set_index('product_id')
df_product['trend'] = (df_product['qty_end'] - df_product['qty_start']) / n_weeks
df_product = df_product['product_name trend noise qty_start qty_end'.split()]

# markets
n_markets = 20
df_market = pd.DataFrame({
    'market_id': range(n_markets),
    'market_name': ['market %d' % i for i in range(n_markets)],
    'period': np.random.choice([7, 13, 52], size=n_markets),
    'amplitude': np.random.uniform(0, 0.5, n_markets)
    }).set_index('market_id')
df_market['phase'] = df_market.period.apply(lambda z: np.random.choice([0.5*z, -0.5*z]))
df_market = df_market['market_name period amplitude phase'.split()]

# time series
df = pd.DataFrame(columns='product_id market_id week_id demand'.split())
for p, m in product(df_product.index, df_market.index):
    x = base_signal(
        n_weeks,
        df_product.iloc[p]['qty_start'],
        df_product.iloc[p]['qty_end'],
        df_product.iloc[p]['noise']
    )*seasonality(
        n_weeks,
        df_market.iloc[m]['period'],
        df_market.iloc[m]['phase'],
        df_market.iloc[m]['amplitude']
    )
    df = df.append(pd.DataFrame({'product_id': p,
                                 'market_id': m,
                                 'week_id': range(n_weeks),
                                 'demand': x
                                 })
                   )
df.set_index('product_id market_id week_id'.split(), inplace=True)

# ------------------------------------------------------------------------------------------------
# Dash app
# time series bar plot with two dimension filters

app = dash.Dash()

demand_graph = dcc.Graph(id='demand-graph')

filters = html.Div([
    html.Div([
        dt.DataTable(
            rows=df_product.to_dict('records'),
            columns=df_product.columns,
            row_selectable=True,
            filterable=True,
            sortable=True,
            selected_row_indices=list(df_product.index),  # all rows selected by default
            id='product-datatable'
        )
    ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dt.DataTable(
            rows=df_market.to_dict('records'),
            columns=df_market.columns,
            row_selectable=True,
            filterable=True,
            sortable=True,
            selected_row_indices=list(df_market.index),  # all rows selected by default
            id='market-datatable'
        )
    ], style={'width': '50%', 'display': 'inline-block'})
])

app.layout = html.Div(children=[demand_graph, filters])


@app.callback(
    Output('demand-graph', 'figure'),
    [Input('product-datatable', 'selected_row_indices'),
     Input('market-datatable', 'selected_row_indices')])
def update_figure(selected_products, selected_markets):
    # filter and group
    dff = df.loc[tuple([selected_products, selected_markets, slice(None)])]
    df_chart = dff.groupby('week_id').sum()

    data = [go.Bar(x=df_chart.index, y=df_chart['demand'], name='demand')]

    title = 'Demand data for %d products and %d markets' % (len(selected_products), len(selected_markets))
    layout = go.Layout(title=title)

    return {'data': data, 'layout': layout}


if __name__ == '__main__':
    app.run_server(debug=True)
