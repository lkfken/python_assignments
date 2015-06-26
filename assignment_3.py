__author__ = 'kleung'

x = 15
target = 10

if x > target:
    print "{} is greater than {}".format(x, target)
elif x == target:
    print "{} is equal to {}".format(x, target)
else:
    print "{} is less than {}".format(x, target)


astr = "Hello world"
try:
    istr = int(astr)
except:
    istr = -1
print 'First', istr

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print 'Second', istr
