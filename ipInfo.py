#!/usr/bin/env python

import time

def sanitize_data(data):
	if data[0] == '\n':
		data = data[1:]
	if data[-1] == '\n':
		data = data[:-1]
	return data 

def shodan_search_host(ip):
    try:
        host = api.host(ip)
        hostname = 'N/A'
        if len(host['hostnames']) > 0:
            hostname = host['hostnames'][0]
        res =  "##### Basic information\n\n"
        res += "| {} | ({}) |\n|:-|:-|\n".format(host['ip_str'], hostname)
        res += "| City | {} |\n".format(host.get('city', 'n/a'))
        res += "| Country | {} |\n".format(host.get('country_name', 'n/a'))
        res += "| Organization | {} |\n".format(host.get('org', 'n/a'))
        res += "| ISP | {} |\n".format(host.get('isp', 'n/a'))
        res += "| Last Update | {} |\n".format(host.get('last_update', 'n/a'))
        res += "| ASN | {} |\n".format(host.get('asn', 'n/a'))

        res += "\n\n\n##### Additional details for open ports\n\n\n"
        for item in host['data']:
            res += "***Port***: {}\n".format(item['port'])
            res += "```\n{}```\n\n".format(sanitize_data(item['data']))

        res += "\n\n\nMore information on Shodan at: [https://www.shodan.io/host/{}](https://www.shodan.io/host/{})".format(host['ip_str'], host['ip_str'])
    except Exception as e:
        print (e)
        res = "***No data available for the IP {}.***".format(ip)
    return res 

if __name__ == '__main__':
	try:
		import shodan
	except ImportError:
		print ("Error while importing shodan.")

	SHODAN_API_KEY = ""
	api = shodan.Shodan(SHODAN_API_KEY)

	info = shodan_search_host('8.8.8.8')
	print (info)
