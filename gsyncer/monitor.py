import re
from wsgiref.simple_server import make_server


#def hello_world_app(environ,start_response):
#    status = '200 OK'
#    headers = [('Content-type','text/plain')]
#    print environ
#
#    start_response(status,headers)
#
#    return ["hello world"]


def event_analyst(environ,start_response):
    
    status = '200 OK'
    headers = [('Content-type','text/plain')]

    start_response(status,headers)
    if environ['REQUEST_METHOD']!='POST':
        return ['Error HTTP method: please use post']
    else:
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH',0))
        except (ValueError):
            request_body_size = 0

        request_body = environ['wsgi.input'].read(request_body_size) 
        print request_body
        return [str(request_body)]
    
    
    

def not_found(environ,start_response):
    start_response('404 NOT FOUND',[('Content-type','text/plain')])
    return ['Not Found']

urls = [
    (r'^$',hello_world_app),
    (r'push_event$',event_analyst)
]


def monitor(environ,start_response):
    status = '200 OK'
    headers = [('Content-type','text/plain')]
    path = environ.get('PATH_INFO','').lstrip('/')
    for regex,callback in urls:
        match = re.search(regex,path)
        if match is not None:
            return callback(environ,start_response)

    return not_found(environ,start_response)


if __name__ == '__main__':

    httpd = make_server('',8080,monitor)
    print "Serving on port 8080"
    httpd.serve_forever()
