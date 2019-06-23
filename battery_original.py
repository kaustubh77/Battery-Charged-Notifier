import getpass
import os
import time
import winsound
import psutil
import numpy as np
import matplotlib.pyplot as plt
import ctypes
import matplotlib.animation as animation

USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
	if file_path == "":
		file_path = os.path.dirname(os.path.realpath(__file__))
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % file_path)

fre=2500
dur=3000

battery=psutil.sensors_battery()
plugged = battery.power_plugged
percent=str(battery.percent)
i=0

Alert_status97=1
Alert_status98=1
Alert_status99=1
Alert_status100=1
Alert_status15=1
Alert_status93=1
Alert_status95=1

while(1):

	 if(percent=='50' or percent=='51' or percent=='52' or percent=='53' or percent=='54' or percent=='85' or percent=='84' or percent=='86' or percent=='87' or percent=='88'):
			 Alert_status100=1
			 Alert_status15=1
			 Alert_status97=1
			 Alert_status98=1
			 Alert_status99=1

	 if(percent=='97' and Alert_status97==1 and plugged==True):
			 winsound.Beep(fre,dur)
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 97% !!", "Battery Notifier", 0)
			 Alert_status97=0

	 if(percent=='98' and Alert_status98==1 and plugged==True):
			 winsound.Beep(fre,dur)
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 98% !!", "Battery Notifier", 0)
			 Alert_status98=0

	 if(percent=='99' and Alert_status99==1 and plugged==True):
			 winsound.Beep(fre,dur)
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 99% !!", "Battery Notifier", 0)
			 Alert_status99=0

	 if(percent=='100' and Alert_status100==1 and plugged==True):
			 winsound.Beep(fre*2,dur*4)
			 print("Laptop Charged, Unplug the charger right now!")
			 ctypes.windll.user32.MessageBoxW(0, "Laptop Charged!!", "Battery Notifier", 0)
			 Alert_status100=0	 

	 if(percent=='15' and Alert_status15==1 and plugged==False):
			 winsound.Beep(fre*2,dur*4)
			 print("Plug in the charger immediately")

	 battery=psutil.sensors_battery()
	 time.sleep(60)
	 percent=str(battery.percent)
	 plugged = battery.power_plugged
	 i=i+1
	 print(str(i)+". Current battery power = "+percent+"% ====== Time : "+str(time.ctime()))