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
fchars = [u"\U0001D622", u"\U0001D623", u"\U0001D624", u"\U0001D625", u"\U0001D626", u"\U0001D627", u"\U0001D628", u"\U0001D629", u"\U0001D62A", u"\U0001D62B", u"\U0001D62C", u"\U0001D62D", u"\U0001D62E", u"\U0001D62F", u"\U0001D630", u"\U0001D631", u"\U0001D632", u"\U0001D633", u"\U0001D634", u"\U0001D635", u"\U0001D636", u"\U0001D637", u"\U0001D638", u"\U0001D639", u"\U0001D63A", u"\U0001D63B", u"\U0001D608", u"\U0001D609", u"\U0001D60A", u"\U0001D60B", u"\U0001D60C", u"\U0001D60D", u"\U0001D60E", u"\U0001D60F", u"\U0001D610", u"\U0001D611", u"\U0001D612", u"\U0001D613", u"\U0001D614", u"\U0001D615", u"\U0001D616", u"\U0001D617", u"\U0001D618", u"\U0001D619", u"\U0001D61A", u"\U0001D61B", u"\U0001D61C", u"\U0001D61D", u"\U0001D61E", u"\U0001D61F", u"\U0001D620", u"\U0001D621"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))