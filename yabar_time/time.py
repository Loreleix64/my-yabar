# -*- coding: utf-8 -*-
import sys  

reload(sys)  
import datetime
sys.setdefaultencoding('utf8')
now = datetime.datetime.now()

y = now.year
m = now.month
d = now.day
h  = now.hour
mi = str(now.minute)
s = str(now.second)

if int(mi) < 10:
	mi = str(0) + str(mi)
	
if int(s) < 10:
	s = str(0) + str(s)
	
print "⌚ %d-%-d-%d %d:%s:%s" % (m, d, y, h, mi, s)
