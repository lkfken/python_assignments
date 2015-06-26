__author__ = 'kleung'

# 3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# 1) Pay the hourly rate for the hours up to 40 and
# 2) 1.5 times the hourly rate for all hours worked above 40 hours.
#
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

OVERTIME_RATE = 1.5
MAX_REGULAR_HOURS = 40

hrs = int(raw_input("Enter hours: "))
rate = float(raw_input("Enter rate: "))

if hrs > MAX_REGULAR_HOURS:
    ot_amt = (hrs - MAX_REGULAR_HOURS) * (rate * OVERTIME_RATE)
    amt = MAX_REGULAR_HOURS * rate
else:
    ot_amt = 0.0
    amt = hrs * rate

total = ot_amt + amt

print(total)
