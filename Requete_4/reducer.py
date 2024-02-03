#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

customer_orders = {}

# Collect orders per customer
for line in sys.stdin:
    customer_id, total = line.strip().split('\t')
    if customer_id not in customer_orders:
        customer_orders[customer_id] = []
    customer_orders[customer_id].append(int(total))

# Calculate average order amount per customer
for customer_id, orders in customer_orders.items():
    avg_order_amount = sum(orders) / len(orders)
    print('%s\t%s' % (customer_id, avg_order_amount))
