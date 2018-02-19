#!/usr/bin/env python

import collections
import subprocess

count = collections.Counter()
lsof = subprocess.Popen('lsof', stdout=subprocess.PIPE)
while True:
    line = lsof.stdout.readline().rstrip()
    if not line:
        break
    data = line.rsplit()
    if data[1].isdigit():
        count[data[1]] += 1

od = collections.OrderedDict(sorted(count.items(), key=lambda x:int(x[0])))
print 'PID\tOpened files'
for key, value in od.items():
    print '%s\t%d' % (key, value)
