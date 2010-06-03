#! /usr/bin/python
#! coding: utf-8
# pylint: disable-msg=W0311
from os import system, chdir
from os.path import dirname
from lib.text_processing import get_text
from settings import BACKEND_PORTS, STATIC_FILES

#----- Build NginX -----
def build_nginx():
  chdir("deps/nginx")
  cmd = """./configure --without-http_autoindex_module 
                       --without-http_ssi_module 
                       --without-http_userid_module 
                       --without-http_auth_basic_module 
                       --without-http_geo_module 
                       --without-http_fastcgi_module 
                       --without-http_empty_gif_module 
                       --prefix=%s""" % ('bin/nginx')
  system(cmd)
  system('make')
  system('make install')
  
  system("cd ../../")
  cmd = 'cp -f %s %s/bin/nginx/conf' % ('conf/nginx.conf', "bin/nginx/conf")
  system(cmd)
  
def update_nginx_config():
    conf = open('bin/nginx/conf/nginx.conf').read()
    
    # change static files directory
    s = get_text('root ', ';', conf)[0]
    conf = conf.replace(s, STATIC_FILES)
    
    # change frontendports
    s = get_text('upstream backends {', '}', conf)[0]
    
    ## generate new config string
    _s = 'server 127.0.0.1:%s;\n\t'
    new_backends = '\n\t'
    for port in BACKEND_PORTS:
        new_backends = new_backends + _s % port
    
    conf = conf.replace(s, new_backends)

    # write new config
    f = open('bin/nginx/conf/nginx.conf', 'w')
    f.write(conf)  
    
if __name__ == "__main__":
  build_nginx()
  update_nginx_config()