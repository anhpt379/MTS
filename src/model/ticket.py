#! /usr/bin/env python
#! coding: utf-8
# pylint: disable-msg=W0311
from cassandra.ttypes import NotFoundException
from lib.database import Database
from lib.barcode import Encoder
from lib.secure import Secure
from settings import AES_SECRET_FILE
from time import time
from hashlib import md5

class TicketSystem:
  def __init__(self):
    self.tdb = Database(column_family="Thông tin vé")
    self.index = Database(column_family="Tìm kiếm")
    self.barcode = Encoder()
    self.secure = Secure()
  
  def add(self, ticket_info):
    """
    Thêm vé vào danh sách vé chưa bán
    ticket_info là một từ điển tương tự như sau:
    ticket_info = {"Từ": "Hà Nội",
                   "Đến": "Thanh Hóa",
                   "Ngày": "26/5/2010",
                   "Giờ xuất phát": "3:30"}
    Trả về:
    - ticket_id nếu thành công
    - None nếu không thành công
    """
    try: 
      ticket_id = md5(str(ticket_info)).hexdigest()
      self.tdb.insert(ticket_id, ticket_info)
      self.index.insert("Vé chưa bán", {ticket_id: str(time())})
      for key in ticket_info.keys():
        self.index.insert(key, {ticket_id: str(time())})
        self.index.insert("%s: %s" % (key, ticket_info[key]),
                             {ticket_id: str(time())})
      return ticket_id
    except KeyError:
      return None
  
  def buy(self, ticket_id, user_id=None):
    """
    Trả về giá trị thời gian khi thực hiện xong
    Nếu gặp lỗi trả về None
    """
    try:
      self.tdb.insert(ticket_id, {"Người mua": str(user_id)})
      self.index.insert("Vé đã bán", {ticket_id: str(time())})
      self.index.remove("Vé chưa bán", ticket_id)
      ticket_info = self.tdb.get(ticket_id)
      for key in ticket_info.keys():
        self.index.remove(key, ticket_id)
        self.index.remove("%s: %s" % (key, ticket_info[key]), ticket_id)
      ticket_id = self.secure.aes_encode(ticket_id, AES_SECRET_FILE)
      barcode_image = self.barcode.qrcode(ticket_id)
      self.tdb.insert(ticket_id, {"Barcode Image": barcode_image})
      # TODO: write log
      return barcode_image
    except KeyError:
      return None
    
  def get_info(self, ticket_id, key=None):
    try:
      if key:
        return self.tdb.get(ticket_id)[key]
      return self.tdb.get(ticket_id)
    except KeyError:
      return None
  
  def available_list(self):
    return self.index.get("Vé chưa bán").keys()
  
  def check(self, encrypted_ticket_id):
    try:
      ticket_id = self.secure.aes_decode(encrypted_ticket_id, AES_SECRET_FILE)
      self.tdb.get(ticket_id)
      return 1
    except (NotFoundException, ValueError):
      return 0
  
  def resend(self, ticket_id):
    """ Gửi lại vé cho người chủ thực sự nếu có tranh chấp xảy ra
    """
    pass
    
  
  def search(self, query):
    """
    query là một chuỗi gồm tên trường và giá trị
      query = "Từ: Hà Nội"
    kết quả trả về sẽ là các vé chưa bán thỏa mãn điều kiện
    """
    try:
      match_ids = self.index.get(query).keys()
      results = []
      for id in match_ids:
        result = self.tdb.get(id)
        results.append(result)
      return results
    except NotFoundException:
      return []
  
  def notification(self):
    pass


if __name__ == "__main__":
  tdb = TicketSystem()
  print tdb.add({"Từ": "Hà Nội",
                       "Đến": "Thanh Hóa",
                       "Ngày": "25/04/2010",
                       "Giờ xuất phát": "5:55", # AM
                       "Toa": "9",
                       "Giá vé": "73000", # VNĐ
                       "Loại": "Ngồi mềm điều hòa"
                         })
  print tdb.add({"Từ": "Hà Nội",
         "Đến": "Thành phố Hồ Chí Minh",
         "Ngày": "25/04/2010",
         "Giờ xuất phát": "5:55", # AM
         "Toa": "10",
         "Giá vé": "73000", # VNĐ
         "Loại": "Ngồi mềm điều hòa"
           })
#  print tdb.available_list()
  ticket_id = tdb.available_list()[0]
  print ticket_id
#  print "Kết quả tìm kiếm\n", len(tdb.search("Đến: Thành phố Hồ Chí Minh"))
#  print
#  print tdb.get_info(ticket_id)["Đến"]
  print tdb.buy(ticket_id)
  print tdb.check('cfff3b54920bf5e7cb7f393d853b5c20')
#  print "Kết quả tìm kiếm\n", len(tdb.search("Toa: 10"))
#  