#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sys import stdin, stdout
import subprocess

def getClipboardData():
 p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
 retcode = p.wait()
 data = p.stdout.read()
 return data

pchars = u"abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890qQ"
fchars = [u"\U00001D43", u"\U00001D47", u"\U00001D9C", u"\U00001D48", u"\U00001D49", u"\U00001DA0", u"\U00001D4D", u"\U000002B0", u"\U00002071", u"\U000002B2", u"\U00001D4F", u"\U000002E1", u"\U00001D50", u"\U0000207F", u"\U00001D52", u"\U00001D56", u"\U000002B3", u"\U000002E2", u"\U00001D57", u"\U00001D58", u"\U00001D5B", u"\U000002B7", u"\U000002E3", u"\U000002B8", u"\U00001DBB", u"\U00001D2C", u"\U00001D2E", u"\U00001D9C", u"\U00001D30", u"\U00001D31", u"\U00001DA0", u"\U00001D33", u"\U00001D34", u"\U00001D35", u"\U00001D36", u"\U00001D37", u"\U00001D38", u"\U00001D39", u"\U00001D3A", u"\U00001D3C", u"\U00001D3E", u"\U00001D3F", u"\U000002E2", u"\U00001D40", u"\U00001D41", u"\U00002C7D", u"\U00001D42", u"\U000002E3", u"\U000002B8", u"\U00001DBB", u"\U000000B9", u"\U000000B2", u"\U000000B3", u"\U00002074", u"\U00002075", u"\U00002076", u"\U00002077", u"\U00002078", u"\U00002079", u"\U00002070", "q", "Q"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))