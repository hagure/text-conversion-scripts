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
fchars = [u"\U0001D482", u"\U0001D483", u"\U0001D484", u"\U0001D485", u"\U0001D486", u"\U0001D487", u"\U0001D488", u"\U0001D489", u"\U0001D48A", u"\U0001D48B", u"\U0001D48C", u"\U0001D48D", u"\U0001D48E", u"\U0001D48F", u"\U0001D490", u"\U0001D491", u"\U0001D492", u"\U0001D493", u"\U0001D494", u"\U0001D495", u"\U0001D496", u"\U0001D497", u"\U0001D498", u"\U0001D499", u"\U0001D49A", u"\U0001D49B", u"\U0001D468", u"\U0001D469", u"\U0001D46A", u"\U0001D46B", u"\U0001D46C", u"\U0001D46D", u"\U0001D46E", u"\U0001D46F", u"\U0001D470", u"\U0001D471", u"\U0001D472", u"\U0001D473", u"\U0001D474", u"\U0001D475", u"\U0001D476", u"\U0001D477", u"\U0001D478", u"\U0001D479", u"\U0001D47A", u"\U0001D47B", u"\U0001D47C", u"\U0001D47D", u"\U0001D47E", u"\U0001D47F", u"\U0001D480", u"\U0001D481"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))