import re

res=re.findall('a','abaabaaabab') #exactly one a
res1=re.findall('a+','ababaaabab') #exactly one or more
res2=re.findall('a*','ababaababaa') #one or many
res3=re.findall('a?','abaabaaaba')#zero or one
res4=re.findall('a{2}','aabaaabaaaab') #match atleast 2
res5=re.findall('a{2,3}','aabaaabaaaab')#find 2 or 3
print(res)
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)