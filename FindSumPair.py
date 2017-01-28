#1,2,3,4,5,6;5
#Finding pairs of sum 5
a=raw_input()
temp=a.split(';')
b=temp[0]
print b
c=int(temp[1])
k=0
list=b.split(',')
list= map(int,list)
for i in list :
    if c-i in list :
        print str(i)+","+str(c-i)
