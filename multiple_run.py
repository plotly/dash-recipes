from multiple_server import server

import multiple_app1
import multiple_app2

print('multiple 1 {}'.format(multiple_app1.app1.config.routes_pathname_prefix))
print('multiple 1 {}'.format(multiple_app1.app1.url_base_pathname))
print('multiple 2 {}'.format(multiple_app2.app2.config.routes_pathname_prefix))
print('multiple 2 {}'.format(multiple_app2.app2.url_base_pathname))

if __name__ == '__main__':
    server.run()
