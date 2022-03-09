from collections import defaultdict

val1={1:100,'A':200,3:300}
newdict=defaultdict(list,val1)

for key,value in newdict.items():
    print(key,value)

if newdict[4]==500:
    print("value is available")
else:
    print("Value is not available")