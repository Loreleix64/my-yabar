# -*- coding: utf-8 -*-
import subprocess
import sys  
import netifaces as ni

add = ni.ifaddresses('wlp3s0')[2][0]['addr']

reload(sys)  
sys.setdefaultencoding('utf8')
command1 = ['nmcli', '-p', 'd']
p = subprocess.Popen(command1, stdout=subprocess.PIPE)
text1 = p.stdout.read()

list1 = text1.splitlines()

list2 = list1[5].split()

if list2[2] == 'connected':
	print "▼ " + list2[3] + " at " + add
	
else:
	print "⌔ Wi-Fi disconnected!"
