#!/usr/bin/env python

import time

def shodan_search_company(company_name):
	try:
		search_filter = "org:"
		search_filter += "\""
		search_filter += company_name
		search_filter += "\""

		results = api.search(search_filter, page=1)

		print('Shodan results: {}'.format(results['total']))

		ip_list = []
		for result in results['matches']:
			ip_list.append(result['ip_str'] + " " + str(result['port']))

	except Exception as e:
		print (e)
	return ip_list

if __name__ == '__main__':
	try:
		import shodan
	except ImportError:
		print("Error while importing shodan.")

	SHODAN_API_KEY = ""
	api = shodan.Shodan(SHODAN_API_KEY)

	info = shodan_search_company('')
	for i in info:
		print(i)
