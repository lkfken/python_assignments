__author__ = 'kleung'

# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
# if len(fname) < 1: fname = 'assn-8-5/mbox-short.txt'
fh = open(fname)
count = 0
sender = dict()

for line in fh:
    if line.startswith('From '):
        email = line.split(' ')[1]
        sender[email] = sender.get(email, 0) + 1

maxval = 0
winner = []

for email, count in sender.items():
    if maxval < count:
        maxval = count
        winner = [email, count]

winner_email = winner[0]
winner_count = winner[1]
print winner_email, winner_count

