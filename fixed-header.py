import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
# app.css.append_css({'external_url': 'https://codepen.io/plotly/pen/xPpeyG.css'})
# app.css.append_css({
#     'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/5047eb29e4afe01b45b27b1d2f7deda2a942311a/goldman-sachs-report.css'
# })

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                # "https://cdn.rawgit.com/plotly/dash-app-stylesheets/5047eb29e4afe01b45b27b1d2f7deda2a942311a/goldman-sachs-report.css",
                'https://codepen.io/plotly/pen/YEYMBZ.css',
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

goldman_sachs_page = html.Div([
    html.Div([  # subpage 1

        # Row 1 (Header)

        html.Div([

            html.Div([
                html.H5(
                    'Goldman Sachs Strategic Absolute Return Bond II Portfolio'),
                html.H6('A sub-fund of Goldman Sachs Funds, SICAV',
                        style={'color': '#7F90AC'}),
            ], className="nine columns padded"),

            html.Div([
                html.H1(
                    [html.Span('03', style={'opacity': '0.5'}), html.Span('17')]),
                html.H6('Monthly Fund Update')
            ], className="three columns gs-header gs-accent-header padded", style={'float': 'right'}),

        ], className="row gs-header gs-text-header"),

        html.Br([]),

        # Row 2

        html.Div([

            html.Div([
                html.H6('Investor Profile',
                        className="gs-header gs-text-header padded"),

                html.Strong('Investor objective'),
                html.P('Capital appreciation and income.',
                       className='blue-text'),

                html.Strong(
                    'Position in your overall investment portfolio*'),
                html.P('The fund can complement your portfolio.',
                       className='blue-text'),

                html.Strong('The fund is designed for:'),
                html.P('The fund is designed for investors who are looking for a flexible \
                        global investment and sub-investment grade fixed income portfolio \
                        that has the ability to alter its exposure with an emphasis on interest \
                        rates, currencies and credit markets and that seeks to generate returns \
                        through different market conditions with a riskier investment strategy \
                        than GS Strategic Absolute Return Bond I Portfolio.', className='blue-text'),

            ], className="four columns"),

            html.Div([
                html.H6(["Performance (Indexed)"],
                        className="gs-header gs-table-header padded"),
                html.Iframe(src="https://plot.ly/~jackp/17553.embed?modebar=false&link=false&autosize=true", \
                            seamless="seamless", style={'border': '0', 'width': "100%", 'height': "250"})
            ], className="eight columns"),

        ], className="row "),

        # Row 2.5

        html.Div([

            html.Div([
                html.H6('Performance (%)',
                        className="gs-header gs-text-header padded"),
                # html.Table(make_dash_table(df_perf_pc),
                           # className='tiny-header')
            ], className="four columns"),

            html.Div([
                html.P("This is an actively managed fund that is not designed to track its reference benchmark. \
                    Therefore the performance of the fund and the performance of its reference benchmark \
                    may diverge. In addition stated reference benchmark returns do not reflect any management \
                    or other charges to the fund, whereas stated returns of the fund do."),
                html.Strong("Past performance does not guarantee future results, which may vary. \
                    The value of investments and the income derived from investments will fluctuate and \
                    can go down as well as up. A loss of capital may occur.")
            ], className="eight columns"),

        ], className="row "),

        # Row 3

        html.Div([

            html.Div([
                html.H6('Fund Data',
                        className="gs-header gs-text-header padded"),
                # html.Table(make_dash_table(df_fund_data))
            ], className="four columns"),

            html.Div([
                html.H6("Performance Summary (%)",
                        className="gs-header gs-table-header padded"),
                # html.Table(modifed_perf_table, className="reversed"),

                html.H6("Calendar Year Performance (%)",
                        className="gs-header gs-table-header padded"),
                # html.Table(make_dash_table(df_cal_year))
            ], className="eight columns"),

        ], className="row "),

    ], className="subpage"),

], className="page")


app.layout = html.Div([
    html.Div(
        style={
            'height': '100px',
            'backgroundColor': 'lightblue'
        },
        children=html.Div([
            'Report Creator'
        ]),
        className='no-print'
    ),
    html.Div(
        style={
            'height': '500px',
        },
        children=html.Div(className='row', children=[
            html.Div([
                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),


                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),


                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                ),

                html.Div(
                    dcc.Dropdown(),
                    style={'marginBottom': 40}
                )

            ], className='three columns no-print', style={'height': '500px', 'overflowY': 'scroll'}),

            html.Div([
                goldman_sachs_page
            ], className='nine columns printwidth100 noprintscroll')
        ])
    )
])


if __name__ == '__main__':
    app.run_server(debug=True, port=9050)
