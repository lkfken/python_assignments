__author__ = 'kleung'

# 4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time-and-a-half in a function called computepay() and
# use the function to do the computation. The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to -
# you can assume the user types numbers properly.

OVERTIME_RATE = 1.5
MAX_REGULAR_HOURS = 40

def computepay(total_work_hours, hourly_rate):
    if total_work_hours > MAX_REGULAR_HOURS:
        ovetime_pay = (total_work_hours - MAX_REGULAR_HOURS) * (hourly_rate * OVERTIME_RATE)
        regular_pay = MAX_REGULAR_HOURS * hourly_rate
    else:
        ovetime_pay = 0.0
        regular_pay = total_work_hours * hourly_rate
    return ovetime_pay + regular_pay
    
total_work_hours = int(raw_input("Enter hours: "))
hourly_rate = float(raw_input("Enter rate: "))

total_pay = computepay(total_work_hours, hourly_rate)
print total_pay