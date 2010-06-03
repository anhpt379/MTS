#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from lib.core import run, route, TornadoServer

@route('/')
def index():
  return 'Hello World!'

run(server=TornadoServer, port=8080)