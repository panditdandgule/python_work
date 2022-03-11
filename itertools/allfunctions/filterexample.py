"""
The filter() function takes function and a list as arguments. This offers an elegant way
to filter out all the elements of sequance.
"""
li=[5,7,22,97,54,62,77,23]

final_list=list(filter(lambda x:x%2==0,li))

print("Filter even Numbers: ",final_list)