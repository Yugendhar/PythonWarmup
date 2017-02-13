filename="test.txt"
count=0
wcount=0
#to print number of words in each line
with open(filename,'r') as file_content:
    for line in file_content:
        words = line.split()
        count+=1
        print 'Number of words in Line '+str(count)+' : '+str(len(words))

print '------------ --------------'
count=0

#to print number of words of length 4
with open(filename, 'r') as file_content:
    for line in file_content:
        words = line.split()
        wcount=0
        for w in words:
            if len(w)==4 :
                wcount+=1
        count+=1
        print 'Number of words of length 4 in Line '+str(count)+' : '+str(wcount)

print '---------- ----------'
count=0
#to print number of words that start with letter 'a'
with open(filename, 'r') as file_content:
    for line in file_content:
        words = line.split()
        wcount=0
        for w in words:
            if w[0].lower()=='a' :
                wcount+=1
        count+=1
        print 'Number of words that start with letter (a or A) in line '+str(count)+' : '+str(wcount)




