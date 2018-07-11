#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdin, stdout
import subprocess

def getClipboardData():
 p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
 retcode = p.wait()
 data = p.stdout.read()
 return data

pchars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
fchars = [u"\U0001D552", u"\U0001D553", u"\U0001D554", u"\U0001D555", u"\U0001D556", u"\U0001D557", u"\U0001D558", u"\U0001D559", u"\U0001D55A", u"\U0001D55B", u"\U0001D55C", u"\U0001D55D", u"\U0001D55E", u"\U0001D55F", u"\U0001D560", u"\U0001D561", u"\U0001D562", u"\U0001D563", u"\U0001D564", u"\U0001D565", u"\U0001D566", u"\U0001D567", u"\U0001D568", u"\U0001D569", u"\U0001D56A", u"\U0001D56B", u"\U0001D538", u"\U0001D539", u"\U00002102", u"\U0001D53B", u"\U0001D53C", u"\U0001D53D", u"\U0001D53E", u"\U0000210D", u"\U0001D540", u"\U0001D541", u"\U0001D542", u"\U0001D543", u"\U0001D544", u"\U00002115", u"\U0001D546", u"\U00002119", u"\U0000211A", u"\U0000211D", u"\U0001D54A", u"\U0001D54B", u"\U0001D54C", u"\U0001D54D", u"\U0001D54E", u"\U0001D54F", u"\U0001D550", u"\U00002124", u"\U0001D7D9", u"\U0001D7DA", u"\U0001D7DB", u"\U0001D7DC", u"\U0001D7DD", u"\U0001D7DE", u"\U0001D7DF", u"\U0001D7E0", u"\U0001D7E1", u"\U0001D7D8"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))