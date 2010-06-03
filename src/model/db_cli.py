#! /usr/bin/env python
#! coding: utf-8
# pylint: disable-msg=W0311
from lib.database import Database
database = Database(column_family="Tìm kiếm")

ticket = database.get(database.get("Từ: Hà Nội").keys()[0])
for i in ticket.keys():
  print i, ticket[i]