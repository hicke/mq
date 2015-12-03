#!/usr/bin/python
# -*- coding: utf-8 -*-
import httplib
import time

def countUp(num, step, delay):
    while num <= 100:
        print "http://46.101.181.25:5000/volume/4/" + str(num)
        num = num + step
        time.sleep(delay)

def countDown(num, step, delay):
    while num >= 1:
        print "http://46.101.181.25:5000/volume/4/" + str(num)
        num = num - step
        time.sleep(delay)

def httpRequest(method, route):
    conn = httplib.HTTPConnection('localhost', '5000')
    conn.request(method, route)
    response = conn.getresponse()

def infiniteLoop():
    loop = 1
    while loop == 1:
        # countUp(1, 1, 0.025)
        # countDown(100, 1, 0.025)
        num = 1
        step = 1
        delay = 0.025
        while num <= 100:
            num = num + step
            httpRequest("POST", "/volume/1/" + str(num))
            time.sleep(delay)
        while num >= 1:
            num = num - step
            httpRequest("POST", "/volume/1/" + str(num))
            time.sleep(delay)


infiniteLoop()
