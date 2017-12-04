import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Iframe(
        # enable all sandbox features
        # see https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe
        # this prevents javascript from running inside the iframe
        # and other things security reasons
        sandbox='',
        style={'border': 'thin lightgrey solid'},
        srcDoc='''
            <div>
                <h3>IFrame Container</h3>
                <div>This raw HTML is rendered inside an IFrame</div>
            </div>
            <script type="text/javascript">
                alert("This javascript will not be executed")
            </script>
        '''
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
