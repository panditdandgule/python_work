from itertools import compress

final_list=list(compress('ABCDEF',[1,0,1,0,1,1]))

print(final_list)