#!/usr/bin/env python3.4

import concurrent.futures as cf

def calc(num):
    return num*2

with cf.ThreadPoolExecutor(max_workers=4) as pool:
    print(list(pool.map(calc, [1,2,3])))
