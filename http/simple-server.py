from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        respone = {'message': 'Hello World!'}
        self.wfile.write(json.dumps(respone).encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('server is running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    try:
       run_server()
    
    except Exception as e:
       print(e)
    finally:
        print('Done!')