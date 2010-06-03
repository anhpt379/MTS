#! /usr/bin/env python
#! coding: utf-8
# pylint: disable-msg=W0311
import urllib 
import httplib2 
from sample_tickets import tickets
http = httplib2.Http() 
url = 'http://127.0.0.1:8888/add'

#for ticket in tickets: 
#  headers = {'Content-type': 'application/x-www-form-urlencoded'}
#  response, content = http.request(url, 'POST', 
#                                   headers=headers, 
#                                   body=urllib.urlencode(ticket))
#  print content
  
#query = [{'query': 'Từ: Hà Nội'},
#         {'query': 'Đến: Thành phố Hồ Chí Minh'}, 
#         {'query': "Giờ xuất phát: 3:55"}]
#for i in query:
#  headers = {'Content-type': 'application/x-www-form-urlencoded'}
#  url = 'http://127.0.0.1:8888/search'
#  response, content = http.request(url, 'POST', 
#                                   headers=headers, 
#                                   body=urllib.urlencode(i))
#  print content
headers = {'Content-type': 'application/x-www-form-urlencoded'}
request = {'browse': 'Giờ xuất phát'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
url = 'http://127.0.0.1:8888/'
response, content = http.request(url, 'POST', 
                               headers=headers, 
                               body=urllib.urlencode(request))
print response
print content