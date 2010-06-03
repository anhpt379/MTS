#! coding: utf-8
import pycassa as cassa
from settings import CASSANDRA_KEYSPACE, CASSANDRA_HOSTS
#
# Connect to servers
client = cassa.connect(CASSANDRA_HOSTS)
u = cassa.ColumnFamily(client, CASSANDRA_KEYSPACE, "Thông tin vé", super=True)

u.insert('en_vi', {'a': {'asdf': 'asdf'}})
print u.get('en_vi')
##print d.get('en_vi', 'a')

#from api.authentication import Authentication
#
#a = Authentication()
#print a._remove('AloneRoad@Gmail.com')
#print a._register('AloneRoad@Gmail.com', md5('3.').hexdigest(), '01673450799')
##print u.get('tuan anh', super_column='info')['join_time']
