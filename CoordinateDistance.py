#(1, 2) (3, 5)
#find distance
import math
a=raw_input()
for delim in '(':
    a = a.replace(delim, '')
for delim in ',':
    a = a.replace(delim, '')
for delim in ')':
    a = a.replace(delim, '')
print a

print a
a= map(int,a)
print a
print math.sqrt((abs(a[0]-a[2])**2)+abs((a[1]-a[3])**2))
