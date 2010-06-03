#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from lib.core import run, route, TornadoServer, request

@route('/Nha_Ga_HN', method="POST")

def nha_ga_ha_noi():
  try:
    nha_cung_cap = request.POST["nha_cung_cap"]
    loai_ve = request.POST["loai_ve"]
    ngay_di = request.POST["ngay_di"]
    gio = request.POST["gio"]
    ghe = request.POST["ghe"]
    phan_loai = request.POST["phan_loai"]
    toa = request.POST["toa"]
    so_hieu_tau = request.POST["so_hieu_tau"]
    trang_thai_ve = request.POST["trang_thai_ve"]
    # Tìm vé thỏa mãn tất cả các thuộc tính này trong CSDL và đánh dấu lại trạng 
    # thái vé
    
    return "OK"
  except:
    return "Error"


run(server=TornadoServer, port=8000)