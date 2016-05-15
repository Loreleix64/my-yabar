# -*- coding: utf-8 -*-
import subprocess
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
command1 = ['upower', '-i', '/org/freedesktop/UPower/devices/battery_BAT0']
p = subprocess.Popen(command1, stdout=subprocess.PIPE)
text1 = p.stdout.read()

list1 = text1.splitlines()

per = ""
state = ""

for lines in list1:
	if "percentage" in lines:
		perline = lines.split()
		per = perline[1]
		
	if state in lines:
		stline = lines.split()
		
		if stline[1] == "discharging":
			state = "Discharging"
			
		elif stline[1] == "fully-charged":
			state = "On AC"
			
		else:
			state = "Charging"

statestring = "⚡ " + per
print statestring
