dict={"1":"one","2":"Two"}
print "user iter items"
for i,j in dict.iteritems():
    print i,j

print "using items"
for i,j in dict.items():
    print i,j

#list options


lis = [1,3,5,6,7,8,1]
print lis
print "reverse list"
print reversed(lis)
for i in reversed(lis):
    print i
print "sorted list and remove duplicates-- sorted() -- set(--)"

print sorted(lis)
print sorted(set(lis))
print "using reverse() returns None"
lis.reverse()
print ''.join(str(lis))
 
