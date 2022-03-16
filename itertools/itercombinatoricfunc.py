from itertools import product,permutations,combinations,combinations_with_replacement


values=[1,2,3]
productresult=list(product(values,repeat=2))
print("It will print SELF,FORWARD,BACKWORD values:")
print(productresult)
print("**"*40)

permutationsresult=list(permutations(values,r=2))
print("It will print FORWARD,BACKWORD values:")
print(permutationsresult)
print("**"*40)

combinationsresult=list(combinations(values,r=2))
print("It will print only FORWARD values: ")
print(combinationsresult)
print("**"*40)

combreplresult=list(combinations_with_replacement(values,r=2))
print("It will print FORWARD and SELF values: ")
print(combreplresult)
print("**"*40)