#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sys import stdin, stdout

pchars = u"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890."
fchars = u"ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾◎"
bubbler = dict(zip(pchars, fchars))

def bubble(s):
  charList = [ bubbler.get(x, x) for x in s.lower() ]
  return "".join(charList)

stdout.write(bubble(stdin.read()).encode('utf8'))
