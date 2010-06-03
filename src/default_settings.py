#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from os.path import dirname, join
from os import listdir, stat, chdir
from time import strftime, localtime

## Check source to detect update date
#
last_update = []
chdir(dirname(__file__))
folder_list = ['controllers', 'lib', 'model']
for folder in folder_list:
  for i in listdir(folder):
    s = stat(join(folder, i))
    _last_update = s.st_mtime
    last_update.append(_last_update)
last_update.append(stat(__file__).st_mtime)
last_update = strftime("%d-%m-%Y", localtime(max(last_update)))

## Prefix of all response
#
INFO = {"version": "0.9.1",
        "last_update": last_update}

## Security
#
AES_SECRET_FILE = '/home/Workspace/MTS/src/lib/secret'

## System Configuration
#
APPLICATION_NAME = "Mobile Ticket System"
APPLICATION_VERSION = "0.9.1"
BACKEND_PORTS = [9000, 9001, 9002, 9003]
FRONTEND_PORT = [80]

STATIC_FILES = join(dirname(__file__), "static")
DATA_DIRECTORY = join(dirname(__file__), "data")
BARCODE_DIRECTORY = join(DATA_DIRECTORY, "barcodes")

CASSANDRA_KEYSPACE = 'MTS'  # Giống thiết lập trong storage-conf.xml
CASSANDRA_HOSTS = ['localhost:9160', ]