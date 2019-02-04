#!/usr/bin/env python

import time

try:
	import shodan
except ImportError:
	print ("Error while importing shodan.")

SHODAN_API_KEY = ""
api = shodan.Shodan(SHODAN_API_KEY)

try:
	info = api.info

	print (time.strftime("%Y%m%d_%H-%M") + " shodan info: ")
	print (info)

except shodan.APIError as e:
	print ("Error: %s" % e)
