__author__ = 'kleung'

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number.
# input: [4, 5, 'bad data', 7, 'done']

list = []

while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        list.append(num)
    except ValueError as err:
        print('Invalid input')

sorted_list = sorted(list)
print "Maximum is", sorted_list[-1]
print "Minimum is", sorted_list[0]
