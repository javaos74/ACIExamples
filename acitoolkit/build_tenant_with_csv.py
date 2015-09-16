#!/usr/bin/env python
# -*- coding: utf-8 -*-

from acitoolkit.acitoolkit import *
from credentials import *
import csv
import sys



def load( path):
	vals = []
	with  open(path,'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			vals.append(row)
	return vals

def build_request_body(data):
	basic = data[0]
	tenant = Tenant( basic['tenant'])
	app = AppProfile( basic['app'], tenant)
	context = Context( basic['network'], tenant)
	print 'Setting Tenant %s, AppProfile %s, Private Network %s' %(basic['tenant'], basic['app'], basic['network'])
	for epgbd in data:
		epg = EPG( epgbd['epg'], app)
		bd = BridgeDomain( epgbd['bd'], tenant)
		bd.add_context( context)
		subnet = Subnet('', bd)
		subnet.set_addr( epgbd['gateway'])
		bd.add_subnet( subnet)
		epg.add_bd(bd)

	return tenant


def main():
	description = 'acitoolkit tutorial application'
	creds = Credentials('apic', description)
	args = creds.get()
	data = load( 'mydata.csv')
	tenant = build_request_body( data)
	
	session = Session(args.url, args.login, args.password)
	session.login()
	resp = tenant.push_to_apic(session)
	if resp.ok:
		print 'Success'
	else:
		print resp.status_code, resp.text 


if __name__ == '__main__':
	main()
