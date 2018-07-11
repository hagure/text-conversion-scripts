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
fchars = [u"\U0001D586", u"\U0001D587", u"\U0001D588", u"\U0001D589", u"\U0001D58A", u"\U0001D58B", u"\U0001D58C", u"\U0001D58D", u"\U0001D58E", u"\U0001D58F", u"\U0001D590", u"\U0001D591", u"\U0001D592", u"\U0001D593", u"\U0001D594", u"\U0001D595", u"\U0001D596", u"\U0001D597", u"\U0001D598", u"\U0001D599", u"\U0001D59A", u"\U0001D59B", u"\U0001D59C", u"\U0001D59D", u"\U0001D59E", u"\U0001D59F", u"\U0001D56C", u"\U0001D56D", u"\U0001D56E", u"\U0001D56F", u"\U0001D570", u"\U0001D571", u"\U0001D572", u"\U0001D573", u"\U0001D574", u"\U0001D575", u"\U0001D576", u"\U0001D577", u"\U0001D578", u"\U0001D579", u"\U0001D57A", u"\U0001D57B", u"\U0001D57C", u"\U0001D57D", u"\U0001D57E", u"\U0001D57F", u"\U0001D580", u"\U0001D581", u"\U0001D582", u"\U0001D583", u"\U0001D584", u"\U0001D585"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))