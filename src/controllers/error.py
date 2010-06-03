#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from lib.core import run, route, TornadoServer

@route('/error_400')
def bad_request():
  return str({"error_code": "400"}) 

@route('/error_500')
def internal_server_error():
  return str({"error_code": "500"})

@route('/error_404') 
def not_found():
  return str({"error_code": "404"}) 

@route('/error_405')  
def method_not_allowed():
  return str({"error_code": "405"})
  
if __name__ == '__main__':
  run(server=TornadoServer, port=9999)
  