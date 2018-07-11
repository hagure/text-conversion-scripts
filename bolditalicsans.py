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
fchars = [u"\U0001D656", u"\U0001D657", u"\U0001D658", u"\U0001D659", u"\U0001D65A", u"\U0001D65B", u"\U0001D65C", u"\U0001D65D", u"\U0001D65E", u"\U0001D65F", u"\U0001D660", u"\U0001D661", u"\U0001D662", u"\U0001D663", u"\U0001D664", u"\U0001D665", u"\U0001D666", u"\U0001D667", u"\U0001D668", u"\U0001D669", u"\U0001D66A", u"\U0001D66B", u"\U0001D66C", u"\U0001D66D", u"\U0001D66E", u"\U0001D66F", u"\U0001D63C", u"\U0001D63D", u"\U0001D63E", u"\U0001D63F", u"\U0001D640", u"\U0001D641", u"\U0001D642", u"\U0001D643", u"\U0001D644", u"\U0001D645", u"\U0001D646", u"\U0001D647", u"\U0001D648", u"\U0001D649", u"\U0001D64A", u"\U0001D64B", u"\U0001D64C", u"\U0001D64D", u"\U0001D64E", u"\U0001D64F", u"\U0001D650", u"\U0001D651", u"\U0001D652", u"\U0001D653", u"\U0001D654", u"\U0001D655"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))