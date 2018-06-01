#!/usr/bin/env python3
import time # This is required to include time module

## Count the number of ticks from the epoch
ticks = time.time()
print("Number of ticks since 12:00 am, January 1, 1970: " + ticks)

## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(ticks) # pass ticks to localtime
print("The local time touple is: " + myTime)
print("The local time touple year is: " + myTime[0])
print("The local time touple month is: " + myTime[1])
print("The local time touple day is: " + myTime[2])
print("The local time touple hour is: " + myTime[3])
print("The local time touple minute is: " + myTime[4])
print("The local time touple second is: " + myTime[5])
print("The local time touple week is: " + myTime[6])
print("The local time touple year is: " + myTime[7])
print("The local time touple daylight savings is: " + myTime[8]) 