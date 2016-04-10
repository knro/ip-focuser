# HTTP server to be used for testing
#
from bottle import route, run, template, request

@route('/focuser')
def index():
    absPos = request.query.absolutePosition
    backlashSteps = request.query.backlashSteps
    alwaysApproach = request.query.alwaysApproach
    print absPos
    print backlashSteps
    print alwaysApproach
    
    return template('{"uptime":"05:14:12", "absolutePosition":    {{absPos}}, "maxPosition":    100000, "minPosition":    10, rain=rain)', absPos = absPos)

run(host='localhost', port=8080)
