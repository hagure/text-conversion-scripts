#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

unstruck = sys.stdin.read()
struck = u'\u0336'.join(unstruck) + u'\u0336'
sys.stdout.write(struck.encode('utf-8'))


