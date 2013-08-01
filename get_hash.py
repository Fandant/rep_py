# -*-  coding: utf-8 -*-

import sys
import os
import hashlib

argvl = sys.argv
argc = len(argvl)
if argc != 2 :
	print "usage:python %s filename" % argvl[0]
	quit()

fsize = os.path.getsize(argvl[1])
if fsize > 4096*1024**3:
	print "can not calclate hash"
	quit()
	
f = open(argvl[1])
cont = f.read()

print "file path:" + os.path.abspath(argvl[1])
print ("file size:%sbyte" % (fsize))
print "MD5:\t" + hashlib.md5(cont).hexdigest()
print "SHA1:\t" + hashlib.sha1(cont).hexdigest()
print "SHA256:\t" + hashlib.sha256(cont).hexdigest()
