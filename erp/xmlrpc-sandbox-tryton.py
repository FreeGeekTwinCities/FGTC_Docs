#!/usr/bin/python
import xmlrpclib
import sys

endpoint = sys.argv[1]
server = xmlrpclib.ServerProxy(endpoint)

try:
    server_method_list = server.system.listMethods()
    user_id, session = server.common.db.login(sys.argv[2], sys.argv[3])
    context = server.model.res.user.get_preferences(user_id, session, True, {})
    request_ids = server.model.res.request.search(user_id, session, [], 0, 10, False, context)
    print request_ids
except xmlrpclib.ProtocolError, err:
    print "A protocol error occurred"
    print "URL: %s" % err.url
    print "HTTP/HTTPS headers: %s" % err.headers
    print "Error code: %d" % err.errcode
    print "Error message: %s" % err.errmsg
except xmlrpclib.Fault, err:
    print "A fault occurred"
    print "Fault code: %d" % err.faultCode
    print "Fault string: %s" % err.faultString


