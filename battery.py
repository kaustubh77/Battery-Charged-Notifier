
'''
Author: Kaustubh Butte
'''

#Import all required libraries
import getpass
import os
import time
import winsound
import psutil
import numpy as np
import matplotlib.pyplot as plt
import ctypes

#We are using the notify_run API to send battery charging alert push notifications to user's devices over the internet
from notify_run import Notify

''' Calling add_to_startup() function will add the given file to shell:startup
	and therefore the script starts working in background everytime 
	the system is switched on. No need to call this function more than once.	
'''
USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
	if file_path == "":
		file_path = os.path.dirname(os.path.realpath(__file__))
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % file_path)

#Creating the object of class Notify for us to be able to call its functions
notify=Notify()

#setting the frequency and duration of the beep
fre=2500
dur=3000

#Creating the object of class sensors_battery for us to be able to call its functions
battery=psutil.sensors_battery()

#plugged tells if the laptop is still on charging or not
plugged = battery.power_plugged

#Converting battery percent for printing purpose
percent=str(battery.percent)

#i is the index of the entry number in console
i=0

#Alert_statusxx is the boolean that decides whether beep user should be alerted or not at xx percent of the battery 
Alert_status97=1
Alert_status98=1
Alert_status99=1
Alert_status100=1
Alert_status15=1
Alert_status93=1
Alert_status95=1

while(1):
	 #When the following percentages are reached, all the Alertstatusxx are set to 1 so that hence onwards user gets notified
	 if(percent=='50' or percent=='51' or percent=='52' or percent=='53' or percent=='54' or percent=='85' or percent=='84' or percent=='86' or percent=='87' or percent=='88'):
			 Alert_status100=1
			 Alert_status15=1
			 Alert_status97=1
			 Alert_status98=1
			 Alert_status99=1
			 Alert_status93=1
			 Alert_status95=1
	 if(percent=='93' and Alert_status93==1 and plugged==True):

	 		 #Creates a sound with given frequency for the set duration
			 winsound.Beep(fre,dur)

			 #Displays a dialog box Displaying the battery percent.
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 93% !!", "Battery Notifier", 0)

			 #Sends a notification to the laptop and also to the mobile of the user. 
			 #User can setup notification option on as many devices as he wants.
			 #Instructions for this are given above 
			 notify.send('Laptop charged to 93%')

			 #Set the Alertstatusxx to 0 to avoid alerting the user again for the same battery percent once again
			 Alert_status93=0

	 if(percent=='95' and Alert_status95==1 and plugged==True):
			 winsound.Beep(fre,dur)
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 95% !!", "Battery Notifier", 0)
			 notify.send('Laptop charged to 95%')
			 Alert_status95=0

	 if(percent=='97' and Alert_status97==1 and plugged==True):
			 winsound.Beep(fre,dur)
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 97% !!", "Battery Notifier", 0)
			 notify.send('Laptop charged to 97%')
			 Alert_status97=0

	 if(percent=='98' and Alert_status98==1 and plugged==True):
			 winsound.Beep(fre,dur)
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 98% !!", "Battery Notifier", 0)
			 notify.send('Laptop charged to 98%')
			 Alert_status98=0

	 if(percent=='99' and Alert_status99==1 and plugged==True):
			 winsound.Beep(fre,dur)
			 ctypes.windll.user32.MessageBoxW(0, "Battery at 99% !!", "Battery Notifier", 0)
			 notify.send('Laptop charged to 99%')
			 Alert_status99=0

	 if(percent=='100' and Alert_status100==1 and plugged==True):
			 winsound.Beep(fre*2,dur*4)
			 print("Laptop Charged, Unplug the charger right now!")
			 ctypes.windll.user32.MessageBoxW(0, "Laptop Charged!!", "Battery Notifier", 0)
			 notify.send('Laptop charged to 100%')
			 Alert_status100=0	 

	 if(percent=='15' and Alert_status15==1 and plugged==False):
			 winsound.Beep(fre*2,dur*4)
			 notify.send('Laptop battery about to die. At 15% currently')
			 print("Plug in the charger immediately")

	 battery=psutil.sensors_battery()

	 #Wait for one minute for reading next battery percentage data
	 time.sleep(60)

	 #Checks battery percent again 
	 percent=str(battery.percent)

	 #Checks if the charger is still plugged in
	 plugged = battery.power_plugged

	 #Increment the index of the console logs
	 i=i+1

	 #Print the battery level in percentage along with date and time on the console/terminal
	 print(str(i)+". Current battery power = "+percent+"% ====== Time : "+str(time.ctime()))