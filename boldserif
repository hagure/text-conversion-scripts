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
fchars = [u"\U0001D41A", u"\U0001D41B", u"\U0001D41C", u"\U0001D41D", u"\U0001D41E", u"\U0001D41F", u"\U0001D420", u"\U0001D421", u"\U0001D422", u"\U0001D423", u"\U0001D424", u"\U0001D425", u"\U0001D426", u"\U0001D427", u"\U0001D428", u"\U0001D429", u"\U0001D42A", u"\U0001D42B", u"\U0001D42C", u"\U0001D42D", u"\U0001D42E", u"\U0001D42F", u"\U0001D430", u"\U0001D431", u"\U0001D432", u"\U0001D433", u"\U0001D400", u"\U0001D401", u"\U0001D402", u"\U0001D403", u"\U0001D404", u"\U0001D405", u"\U0001D406", u"\U0001D407", u"\U0001D408", u"\U0001D409", u"\U0001D40A", u"\U0001D40B", u"\U0001D40C", u"\U0001D40D", u"\U0001D40E", u"\U0001D40F", u"\U0001D410", u"\U0001D411", u"\U0001D412", u"\U0001D413", u"\U0001D414", u"\U0001D415", u"\U0001D416", u"\U0001D417", u"\U0001D418", u"\U0001D419", u"\U0001D7CF", u"\U0001D7D0", u"\U0001D7D1", u"\U0001D7D2", u"\U0001D7D3", u"\U0001D7D4", u"\U0001D7D5", u"\U0001D7D6", u"\U0001D7D7", u"\U0001D7CE"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))