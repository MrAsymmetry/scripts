# Script for quickly calculating fatigue in Hearthstone

import sys

if len(sys.argv) != 3:
	print "\tUsage:\t\tpython fatigue.py cards start"
	sys.exit()

cards = int(sys.argv[1])
start = int(sys.argv[2])

x = 0
sum = 0

while x != cards:
	sum += start
	start += 1
	x+=1

print "Fatigue damage:\t{}".format(sum)
