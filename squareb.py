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
fchars = [u"\U0001F170", u"\U0001F171", u"\U0001F172", u"\U0001F173", u"\U0001F174", u"\U0001F175", u"\U0001F176", u"\U0001F177", u"\U0001F178", u"\U0001F179", u"\U0001F17A", u"\U0001F17B", u"\U0001F17C", u"\U0001F17D", u"\U0001F17E", u"\U0001F17F", u"\U0001F180", u"\U0001F181", u"\U0001F182", u"\U0001F183", u"\U0001F184", u"\U0001F185", u"\U0001F186", u"\U0001F187", u"\U0001F188", u"\U0001F189", u"\U0001F170", u"\U0001F171", u"\U0001F172", u"\U0001F173", u"\U0001F174", u"\U0001F175", u"\U0001F176", u"\U0001F177", u"\U0001F178", u"\U0001F179", u"\U0001F17A", u"\U0001F17B", u"\U0001F17C", u"\U0001F17D", u"\U0001F17E", u"\U0001F17F", u"\U0001F180", u"\U0001F181", u"\U0001F182", u"\U0001F183", u"\U0001F184", u"\U0001F185", u"\U0001F186", u"\U0001F187", u"\U0001F188", u"\U0001F189"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))