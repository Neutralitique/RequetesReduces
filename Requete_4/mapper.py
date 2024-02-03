#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) == 2:
        customer_id, total = fields
        print('%s\t%s' % (customer_id, total))
