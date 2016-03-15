#!/usr/bin/env python3
import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
cmds = [
    'python3 school.py'
    ]
cmds += cmds
cmds += cmds
#cmds += cmds
while True:
    pool = ThreadPool(5)
    pool.map(os.system, cmds)
    pool.close()
    pool.join()