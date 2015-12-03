#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import json
import os
import httplib
import httpClient



# Get json from sr.se
response = urllib.urlopen('http://api.sr.se/api/v2/episodes/index?programid=2000&format=json&audioquality=hi&page=1&size=1')
data = json.load(response)

# Extract the correct url from json
url = data['episodes'][0]['broadcast']['broadcastfiles'][0]['url']

# Extract correct filename
soundFile = url.split('/')[-1]

# Open correct url
f = urllib.urlopen(url)

# Check if file exists
if os.path.exists(soundFile):
    print("File exists")
else:
    # Open file and set as binary
    fh = open(soundFile, 'wb')
    # Write binary file to disk
    fh.write(f.read())
    # Close file
    fh.close()
    print soundFile
    # Only a test route. Should be changed to AT BL route
    #httpClient.httpRequest("POST", "/play")
