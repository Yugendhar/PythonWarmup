a=raw_input()
str=""
for word in a.split():
    i=0
    for w in word :
        if i%2!=0:
          str+=w
        else :
         str+=w.upper()
        i+=1
    str+=" "
print str.strip()
