#a=raw_input()
text = ""
stopword = ""

while True:
    line = raw_input()
    if line.strip() == stopword:
        break
    text += "%s\n" % line
sum=0
k=0
print text
temp= text.strip().split('\n')
temp= map(int, temp)
print temp
for i in temp:
    sum+=i
print sum
