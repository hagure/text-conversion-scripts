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
fchars = [u"\U0001D68A", u"\U0001D68B", u"\U0001D68C", u"\U0001D68D", u"\U0001D68E", u"\U0001D68F", u"\U0001D690", u"\U0001D691", u"\U0001D692", u"\U0001D693", u"\U0001D694", u"\U0001D695", u"\U0001D696", u"\U0001D697", u"\U0001D698", u"\U0001D699", u"\U0001D69A", u"\U0001D69B", u"\U0001D69C", u"\U0001D69D", u"\U0001D69E", u"\U0001D69F", u"\U0001D6A0", u"\U0001D6A1", u"\U0001D6A2", u"\U0001D6A3", u"\U0001D670", u"\U0001D671", u"\U0001D672", u"\U0001D673", u"\U0001D674", u"\U0001D675", u"\U0001D676", u"\U0001D677", u"\U0001D678", u"\U0001D679", u"\U0001D67A", u"\U0001D67B", u"\U0001D67C", u"\U0001D67D", u"\U0001D67E", u"\U0001D67F", u"\U0001D680", u"\U0001D681", u"\U0001D682", u"\U0001D683", u"\U0001D684", u"\U0001D685", u"\U0001D686", u"\U0001D687", u"\U0001D688", u"\U0001D689"]

mapping = dict(zip(pchars, fchars))

def converter(s):
  charList = [ mapping.get(x, x) for x in s ]
  return "".join(charList)

stdout.write(converter(getClipboardData()).encode('utf8'))