#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) == 2:
        order_id, total = fields
        month = int(order_id) % 100
        print('%d\t%s' % (month, 1))
