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
fchars = [u"\U0001F130", u"\U0001F131", u"\U0001F132", u"\U0001F133", u"\U0001F134", u"\U0001F135", u"\U0001F136", u"\U0001F137", u"\U0001F138", u"\U0001F139", u"\U0001F13A", u"\U0001F13B", u"\U0001F13C", u"\U0001F13D", u"\U0001F13E", u"\U0001F13F", u"\U0001F140", u"\U0001F141", u"\U0001F142", u"\U0001F143", u"\U0001F144", u"\U0001F145", u"\U0001F146", u"\U0001F147", u"\U0001F148", u"\U0001F149", u"\U0001F130", u"\U0001F131", u"\U0001F132", u"\U0001F133", u"\U0001F134", u"\U0001F135", u"\U0001F136", u"\U0001F137", u"\U0001F138", u"\U0001F139", u"\U0001F13A", u"\U0001F13B", u"\U0001F13C", u"\U0001F13D", u"\U0001F13E", u"\U0001F13F", u"\U0001F140", u"\U0001F141", u"\U0001F142", u"\U0001F143", u"\U0001F144", u"\U0001F145", u"\U0001F146", u"\U0001F147", u"\U0001F148", u"\U0001F149"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))