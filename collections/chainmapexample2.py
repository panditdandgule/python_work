from collections import ChainMap

val1 = {1:1001,2:2200,"A":3000}
val2 = {1:1002,2:2400,3:3600,"B":3495}
val3 = {1:1003,"C":555,3:2007,3:3800}
chmp = ChainMap(val1,val2,val3)
print(chmp)
#search --? first mein nh hoga to next mein
print(chmp.get(1)) # 1001
print(chmp.get("B")) #val1 val2 --> 3495
print(chmp.get("C")) #val1 val1 val3 -->555
print(chmp.get("D"))

#only first dict is avaible for update      ONLY FIRST
chmp["D"] = 100  # first dict
chmp["B"] = 200  # first mein

ans = chmp.parents   # val2,val3
ans.get('A')    #None
ans['X'] = 44  #val2
ans = ans.parents   # val3

chmp.new_child({2:34,5:67,3:5})  # creating a first..


#parents --> removes first dict -- and then returns


print(chmp)