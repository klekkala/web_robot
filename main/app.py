import Pyro.core
from cgi import parse_qs

def application(environ, start_response):

    # Connect to Pyro
    movement = Pyro.core.getProxyForURI("PYRONAME://robotmovement")

    parameters = parse_qs(environ['QUERY_STRING'])

    if 'seconds' in parameters and 'direction' in parameters:
        direction = parameters['direction'][0]
        seconds = int(parameters['seconds'][0])

        # Call the appropriate function
        if direction == 'Stop':
           movement.stop()
        elif direction == 'Forwards':
           movement.forward(seconds)
        elif direction == 'Backwards':
           movement.backward(seconds)
        elif direction == 'Left':
           movement.left(seconds)
        elif direction == 'Right':
           movement.right(seconds)
     
        status = '200 OK'

    else:
        status = '400 Bad Request'
    
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(status)))]
    start_response(status, response_headers)
    return [status]
