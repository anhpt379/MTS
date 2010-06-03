#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from lib.pysolr import Solr
from settings import SOLR_SERVER
import re


class Index:
  def __init__(self, host=SOLR_SERVER):
    self.index = Solr(SOLR_SERVER)
    self.ESCAPE_CHARS_RE = re.compile(r'(?<!\\)(?P<char>[&|+\-!(){}[\]^"~*?:])')

  def _escape(self, value):
    """
    Solr/Lucene special characters: + - ! ( ) { } [ ] ^ " ~ * ? : \
    There are also operators && and ||, but we're just going to escape
    the individual ampersand and pipe chars.
    Also, we're not going to escape backslashes!
    http://lucene.apache.org/java/2_9_1/queryparsersyntax.html#Escaping+Special+Characters
    """
    return self.ESCAPE_CHARS_RE.sub(r'\\\g<char>', value)
    
  def add(self, key, content):
    self.index.add([{"id": key, "text": content}])
    self.index.commit()
    return True 

  def remove(self, key):
    return self.index.delete(id=key)
  
  def optimize(self):
    return self.index.optimize()
  
  def search(self, query):
    results = self.index.search(self._escape(query))
    if results:
      return [result["id"] for result in results]
    return None


if __name__ == "__main__":
  index = Index()
  index.add("TicketID_1", "Vé hành khách, ngồi mềm điều hòa, 10:30 ngày 23/05/2010")
  print index.search("hành lửa")
  