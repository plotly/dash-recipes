import flask
import time

server = flask.Flask(__name__)


@server.route('/')
def index():
    return '''
    <html>
        <body>
            <button id="button">Send my greetings</button>
        </body>
        <script type="text/javascript">
            document.getElementById('button').onclick=function(){
                fetch('/submit', {'method': 'post'});
            }
        </script>
    </html>
    '''


@server.route('/submit', methods=['POST'])
def submit():
    print('submit')
    time.sleep(5)
    return ''




if __name__ == '__main__':
    server.run()
