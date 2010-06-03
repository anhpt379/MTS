#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from elaphe import barcode
from datamatrix import DataMatrixEncoder
from hashlib import md5
from os.path import join, basename
from settings import BARCODE_DIRECTORY

class Encoder:
  def __init__(self):
    pass
  
  def qrcode(self, input_string, out_file=None):
    """ Mã hóa chuỗi input_string thành ảnh 126x126 QR Code 
    và lưu dưới tên out_file
    
    >>> from lib.barcode import Encoder
    >>> e = Encoder()
    >>> e.qrcode("Any string (max. 2,953 bytes)")
    True
    >>> e.qrcode("Any string (max. 2,953 bytes)", "test.png")
    True
    >>> e.qrcode("Any string (max. 2,953 bytes)", "test.jpg")
    True
    >>> e.qrcode("Any string (max. 2,953 bytes)", "test.jp")
    False
    >>> e.qrcode("Any string (max. 2,953 bytes)", "test")
    False
    >>> e.qrcode("Any string (max. 2,953 bytes)", "")
    False
    >>> e.qrcode("")
    True
    >>> 
    """
    if out_file is None:
      out_file = join(BARCODE_DIRECTORY, 
                      "%s.jpg" % md5(input_string).hexdigest())
    
    try:
      image = barcode('qrcode', input_string, 
                      options=dict(version=9, eclevel='H'),
                      margin=10, data_mode='8bits')
      print out_file
      # TODO: add binary image to cassandra
      image.save(out_file)
      return basename(out_file)
    except (TypeError, KeyError):
      return None
  
  def datamatrix(self, input_string, out_file=None):
    """ Mã hóa chuỗi input_string (chỉ sử dụng ký tự alphanumberic) thành ảnh 
    sử dụng thuật toán DataMatrix.
   
    >>> from lib.barcode import Encoder
    >>> e = Encoder()
    >>> e.datamatrix("any alphanumberic string")
    True
    >>> e.datamatrix("any alphanumberic string", "test.png")
    True
    >>> e.datamatrix("sử dụng ký tự khác alphanumberic")
    True
    >>> e.datamatrix("")
    True
    >>> 
    """
    if out_file is None:
      out_file = join(BARCODE_DIRECTORY, 
                      "%s.png" % md5(input_string).hexdigest())
    try:
      encoder = DataMatrixEncoder(input_string)
      encoder.save(out_file)
      return basename(out_file)
    except (TypeError, KeyError):
      return None
  
  def azteccode(self, input_string, out_file):
    pass
  
class Decoder:
  def __init__(self):
    pass
  

if __name__ == "__main__":
#  import doctest
#  doctest.testmod()
  e = Encoder()
  input_string = 'G8osNsJsuz1odLKrcU8iiCvJHoXfX3xtqLavK8O87qQUtRSETN9dKYWCf7Oop7QVGICwI1vzFNc2SMqEvBIqVvitZsiMnRNUhvS+ep5Q6GYftBtERtJ3qJ6N6FrLaJL9vHbJ5iK98LIp//1gtRQpPHr3rdVFHKi8H3V9SXwLKv8Kp/P1NvSWfmed5iLhpAdJSJqe2G7EUkG2kW6xw+HjnIr6bFwEPoRo4eMIKBOQLPaDdXUur4EtZdgDCfP/jNhX8FamK493woOaAcgosw8Vp+A+nu4UazqkrXjoVndaHEFNFdeZFhzv+DYLwfcGODCVecOv4huLu//ByT9VwW5gql21xCWAlvhxNtrmjzYNSjfJedQjF4KrAmUSIEnTTTAMmz2fYR4RRQ8Mvl9huoBBBgis+AE1hWPGPbTtBZ+H2d0='
  input_string = '3Pd5jtExLmdcmBm9F+48UTo9JnxH2jFPIRKR+5Qy0BuuRPnkrz0FbZU55DzQANeGrkT55K89BW2VOeQ80ADXhg=='
  print e.qrcode(input_string)
