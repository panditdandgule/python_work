from collections import ChainMap
val1 = {1:1001,2:2200,"A":3000}
val2 = {1:1002,2:2400,3:3600,"B":3495}
val3 = {1:10503,"C":555,3:2007,3:3800}
val4 = {1:10043,"C":555,3:2007,3:3800}
val5 = {1:10033,"C":555,3:2007,3:3800}
val6 = {1:10603,"C":555,3:2007,3:3800}




def get_all_valuesfrom_map(key):
    chmp = ChainMap(val1, val2, val3,val4,val5,val6)
    all_values = []
    if chmp.get(key):
        all_values.append(chmp.get(key))        # first
    flag = True
    while flag:
        chmp = chmp.parents     #first dict remove --> val2, val3   --> val3  -- > 0
        if len(chmp)==0:
            return all_values
        if chmp.get(key):
            all_values.append(chmp.get(key))        # first


print(get_all_valuesfrom_map(1))