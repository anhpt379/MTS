#!/usr/bin/env python
#! coding: utf-8
# pylint: disable-msg=W0311

from Crypto.Cipher import AES
import base64
import os


class Secure:
  def __init__(self):
    # the block size for the cipher object; must be 16, 24, or 32 for AES
    self.BLOCK_SIZE = 32

    # the character used for padding--with a block cipher such as AES, the value
    # you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
    # used to ensure that your value is always a multiple of BLOCK_SIZE
    self.PADDING = '{'
    
    # one-liner to sufficiently pad the text to be encrypted
    self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING
  
  def new_secret_key(self, secret_file="secret"):
    # generate a random secret key
    secret = os.urandom(self.BLOCK_SIZE)
    f = open(secret_file, "w")
    f.write(secret)
    f.close()
    return secret_file
    
  def aes_encode(self, raw_string, secret_file="secret"):
    """
    Sử dụng AES (khác RSA)
    """
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(self.pad(s)))
    cipher = AES.new(open(secret_file).read())
    
    # encode a string
    encoded = EncodeAES(cipher, raw_string)
    return encoded
    
  def aes_decode(self, encoded_string, secret_file="secret"):
    # encrypt with AES, encode with base64
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(self.PADDING)
    cipher = AES.new(open(secret_file).read())
    
    # decode the encoded string
    decoded = DecodeAES(cipher, encoded_string)
    return decoded


if __name__ == "__main__":
  s = Secure()
  file = s.new_secret_key()
  string = s.aes_encode("cfff3b54920bf5e7cb7f393d853b5c20", file)
  print string
  print s.aes_decode(string, file)
  