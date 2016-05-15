# -*- coding: utf-8 -*-
#requires hurry.filesize !!!
import subprocess
import sys  
from hurry.filesize import size

reload(sys)  
sys.setdefaultencoding('utf8')
sys.setdefaultencoding('utf8')
command1 = ['df', '-k']
p = subprocess.Popen(command1, stdout=subprocess.PIPE)
text1 = p.stdout.read()

list1 = text1.splitlines()
list2 = []

for lines in list1:
	if "/dev/mapper/cryptAntergos" in lines:
		list2 = lines.split()
		
print "◎ " +  size(int(list2[3]) * 1024)
