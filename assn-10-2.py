__author__ = 'kleung'

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# Note that the autograder does not have support for the sorted() function.

fname = raw_input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
if len(fname) < 1: fname = 'assn-8-5/mbox-short.txt'
fh = open(fname)
chart = {}

for line in fh:
    if line.startswith('From '):
        words = line.rstrip().split(' ')
        words = filter(len, words)
        timestamp = words[5]
        hour = timestamp.split(':')[0]
        chart[hour] = chart.get(hour, 0) + 1


hours = chart.items()
hours.sort()
for hour, count in hours:
     print hour, count

