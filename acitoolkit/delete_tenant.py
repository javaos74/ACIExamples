#!/usr/bin/env python
# -*- coding: utf-8 -*-

from acitoolkit.acitoolkit import *
from credentials import *
import csv


def load( path):
	vals = []
	with  open(path,'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			vals.append(row)
	return vals

def main():
	description = 'acitoolkit tutorial application'
	creds = Credentials('apic', description)
	args = creds.get()

	data = load( 'mydata.csv')
	tenant = Tenant( data[0]['tenant'])
	tenant.mark_as_deleted()
	session = Session(args.url, args.login, args.password)
	session.login()
	resp = tenant.push_to_apic(session)
	if resp.ok:
		print 'Success'
	else:
		print resp.status_code, resp.text 

if __name__ == '__main__':
	main()