#! /usr/bin/env python
#! coding: utf-8
# pylint: disable-msg=W0311
from operator import itemgetter
from itertools import groupby
from simplejson import dumps
from model import ticket
from lib.core import run, route, request, response, TornadoServer

tdb = ticket.TicketSystem()

@route('/add', method='POST')
def add_ticket():
  try:
    ticket_info = request.POST
    if '-' in ticket_info['Ghế số']:
      start, end = ticket_info['Ghế số'].split('-')
      seats = range(int(start), int(end))
      _info = ticket_info
      for ghe in seats:
        _info['Ghế số'] = str(ghe)
        tdb.add(_info)
    if tdb.add(ticket_info):
      return "200"
    return "500"
  except:
    return "500"
  
@route('/', method='POST')
def browse():
  try:
    type = request.POST['browse']
    results = tdb.search(type)
    # sort by key
    list1 = []
    results.sort(key=itemgetter(type))
    for key, items in groupby(results, itemgetter(type)):
      list1.append({key: list(items)})
    response.charset = 'UTF-8'
    return dumps(list1, indent=2)
  except:
    return "500"

@route('/search', method='POST')
def search():
  try:
    query = request.POST['query']
    results = tdb.search(query)
    return dumps(results, indent=2)
  except KeyboardInterrupt:
    return "500"

@route('/buy', method='POST')
def buy():
  pass


if __name__ == "__main__":
  run(server=TornadoServer, port=8888)