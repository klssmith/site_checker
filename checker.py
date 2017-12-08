#!/usr/bin/env python3

import urllib.request

url = 'http://example.com'

try:
    response = urllib.request.urlopen(url)

    print(response.getcode())
except urllib.error.HTTPError as e:

    print(e.getcode())
