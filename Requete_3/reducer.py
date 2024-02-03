#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

customer = {}

# Load customer data
for line in open('customer.txt'):
    customer_id, _, customer_name = line.strip().split(',')
    customer[customer_id] = customer_name

# Process orders and join with customer data
for line in sys.stdin:
    order_id, total = line.strip().split('\t')
    if order_id in customer:
        print('%s\t%s\t%s' % (customer[order_id], order_id, total))
