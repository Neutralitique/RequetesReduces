#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

current_month = None
total_sales = 0

for line in sys.stdin:
    month, count = line.strip().split('\t')
    if current_month == month:
        total_sales += int(count)
    else:
        if current_month:
            print('%d\t%d' % (current_month, total_sales))
        current_month = month
        total_sales = int(count)

if current_month:
    print('%d\t%d' % (current_month, total_sales))
