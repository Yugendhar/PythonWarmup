inputStr = raw_input().lower()
count = {}
uniqueCount = 0;
for s in inputStr:
  if count.has_key(s):
    count[s] += 1
  else:
    count[s] = 1
print len(count)
for key in count:
  if count[key] == 1:
    uniqueCount = uniqueCount+1
print uniqueCount
