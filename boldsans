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
fchars = [u"\U0001D5EE", u"\U0001D5EF", u"\U0001D5F0", u"\U0001D5F1", u"\U0001D5F2", u"\U0001D5F3", u"\U0001D5F4", u"\U0001D5F5", u"\U0001D5F6", u"\U0001D5F7", u"\U0001D5F8", u"\U0001D5F9", u"\U0001D5FA", u"\U0001D5FB", u"\U0001D5FC", u"\U0001D5FD", u"\U0001D5FE", u"\U0001D5FF", u"\U0001D600", u"\U0001D601", u"\U0001D602", u"\U0001D603", u"\U0001D604", u"\U0001D605", u"\U0001D606", u"\U0001D607", u"\U0001D5D4", u"\U0001D5D5", u"\U0001D5D6", u"\U0001D5D7", u"\U0001D5D8", u"\U0001D5D9", u"\U0001D5DA", u"\U0001D5DB", u"\U0001D5DC", u"\U0001D5DD", u"\U0001D5DE", u"\U0001D5DF", u"\U0001D5E0", u"\U0001D5E1", u"\U0001D5E2", u"\U0001D5E3", u"\U0001D5E4", u"\U0001D5E5", u"\U0001D5E6", u"\U0001D5E7", u"\U0001D5E8", u"\U0001D5E9", u"\U0001D5EA", u"\U0001D5EB", u"\U0001D5EC", u"\U0001D5ED", u"\U0001D7ED", u"\U0001D7EE", u"\U0001D7EF", u"\U0001D7F0", u"\U0001D7F1", u"\U0001D7F2", u"\U0001D7F3", u"\U0001D7F4", u"\U0001D7F5", u"\U0001D7EC"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))