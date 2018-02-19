#!/usr/bin/env python

from collections import OrderedDict, defaultdict
from datetime import datetime, timedelta
import re

fh = open('task_1_2.log', 'r')
d = defaultdict(list)

for line in fh:
    tstamp = re.search('\[.*\]', line).group(0)
    tstamp = re.split('[\[\]]', tstamp)[1]
    tstamp = datetime.strptime(tstamp, '%Y-%m-%d %H:%M:%S.%f')
    text   = re.sub('\[.*\] ', '', line)
    level  = re.split(' ', text)[0]
    msg    = re.sub('^[A-Z]+ ', '', text)
    msg    = ''.join(msg.splitlines())
    req    = re.search('Request (\d+)', msg).group(1)
    list   = d[req]

    if len(list) == 0:
        list = [None] * 4

    if re.match('^Started processing', msg):
        list[0] = tstamp
    elif re.match('^Finished processing', msg):
        list[1] = tstamp

    if re.match('^ERROR', level):
        list[2] = tstamp
        list[3] = re.sub(' for >Request .*', '', msg)

    d[req] = list

od = OrderedDict(sorted(d.items(), key=lambda x:int(x[0])))
for key, values in od.items():
    print('Request %s: ' % (key)),
    if values[1]:
        print('%.3f' % (values[1] - values[0]).seconds)
    else:
        print('-1.000')

print
print 'Errors:'
for key, values in od.items():
    if values[3]:
        print 'Request %s: %s' % (key, values[3])
