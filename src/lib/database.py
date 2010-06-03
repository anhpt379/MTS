#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from pycassa import connect, ColumnFamily
from settings import CASSANDRA_HOSTS, CASSANDRA_KEYSPACE
from hashlib import md5
from string import capwords

class Database:
  def __init__(self, column_family):
    """
    ColumnFamily: 
    - Thông tin người dùng
    - Tìm kiếm 
    - Thông tin vé
    - Nhật ký hệ thống
    - Thông tin nhà cung cấp
    """
    # Connect to Cassandra servers
    client = connect(CASSANDRA_HOSTS)
    self.db = ColumnFamily(client, CASSANDRA_KEYSPACE,
                           column_family, super=False)
  
  def insert(self, key, columns):
    key = md5(capwords(key).lower()).hexdigest()
    return self.db.insert(key, columns)
  
  def get(self, key, columns=None):
    key = md5(capwords(key).lower()).hexdigest()
    return self.db.get(key=key, columns=columns)
  
  def remove(self, key, column=None):
    key = md5(capwords(key).lower()).hexdigest()
    return self.db.remove(key=key, column=column)
  
if __name__ == '__main__':
  db = Database("Thông tin vé")
  print db.insert('Đến: Thành phố Hồ Chí Minh', {'sadf': 'asdf',
                                                 'a': 'asw'})
  print db.get('Đến: Thành phố Hồ Chí Minh')
  print db.remove('Đến: Thành phố Hồ Chí Minh', 'a')
  print db.get('Đến: Thành phố Hồ Chí Minh')['sadf']
  print db.get('Đến: Thành phố Hồ Chí Minh')['a']
  
  

