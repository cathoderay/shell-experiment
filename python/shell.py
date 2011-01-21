#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File: shell.py
    Description: a simple python REPL
"""

__author__ = "raios dot catodicos at gmail dot com"


print """python-shell -- version 0.0.1"""
while True:
    inp = raw_input("¬¬ ")
    try:
        exec(inp)
    except Exception, e:
        print e

