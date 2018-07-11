#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdin, stdout
import subprocess

def getClipboardData():
 p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
 retcode = p.wait()
 data = p.stdout.read()
 return data

pchars = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
fchars = [u"\U0001D4EA", u"\U0001D4EB", u"\U0001D4EC", u"\U0001D4ED", u"\U0001D4EE", u"\U0001D4EF", u"\U0001D4F0", u"\U0001D4F1", u"\U0001D4F2", u"\U0001D4F3", u"\U0001D4F4", u"\U0001D4F5", u"\U0001D4F6", u"\U0001D4F7", u"\U0001D4F8", u"\U0001D4F9", u"\U0001D4FA", u"\U0001D4FB", u"\U0001D4FC", u"\U0001D4FD", u"\U0001D4FE", u"\U0001D4FF", u"\U0001D500", u"\U0001D501", u"\U0001D502", u"\U0001D503", u"\U0001D4D0", u"\U0001D4D1", u"\U0001D4D2", u"\U0001D4D3", u"\U0001D4D4", u"\U0001D4D5", u"\U0001D4D6", u"\U0001D4D7", u"\U0001D4D8", u"\U0001D4D9", u"\U0001D4DA", u"\U0001D4DB", u"\U0001D4DC", u"\U0001D4DD", u"\U0001D4DE", u"\U0001D4DF", u"\U0001D4E0", u"\U0001D4E1", u"\U0001D4E2", u"\U0001D4E3", u"\U0001D4E4", u"\U0001D4E5", u"\U0001D4E6", u"\U0001D4E7", u"\U0001D4E8", u"\U0001D4E9"]

smaller = dict(zip(pchars, fchars))

def cursive(s):
  charList = [ smaller.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(cursive(getClipboardData()).encode('utf8'))