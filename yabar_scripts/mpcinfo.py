# -*- coding: utf-8 -*-
import subprocess
import sys  

reload(sys)
command = ['mpc']
p = subprocess.Popen(command, stdout=subprocess.PIPE)
text = p.stdout.read()

list1 = text.splitlines()

try:
	list2 = list1[1].split()
	info = (list1[0][:28] + '...') if len(list1[0]) > 28 else list1[0]
	if "[playing]" in list1[1]:
		print "▶ " + info + " " + list2[2]
	else:
		print "▋▋ " + info + " " + list2[2]
		
except:
	print "Nothing playing"
