import time

currentTime = time.time()
#set the current time to the time function

totalSeconds = int(currentTime)
currentSeconds = totalSeconds %60
#since a complete seconds in a total of 60 then we get the current seconds by the modulos of the total seconds from the current time
 
totalMinutes = totalSeconds //60
currentMinutes = totalMinutes %60
#since totalminutes is made up of 60 and 60 seconds makes one minutes so we get totalminutes by the division of total seconds and the current minutes by the modulos of the total number of minutes that makes a second

totalHours = totalMinutes //60
currentHours = totalHours %24
#since total number of an hour in a minute is 60 so we divide to get the total number of hours and to get the current hours we get the remainder of the number of hours to make a day


currentHours = str(currentHours)
currentMinutes = str(currentMinutes)
currentSeconds = str(currentSeconds)
print (str(currentHours), str(currentMinutes), str(currentSeconds))
