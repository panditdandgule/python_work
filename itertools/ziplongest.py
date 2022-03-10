"""
zip_longest( iterable1, iterable2, fillval):
This iterator prints the values of iterables alternatively in sequence.
If one of the iterables is printed fully, the remaining values are filled by the values assigned to fillvalue.
Example:
"""
# Python code to demonstrate the working of
# zip_longest()


import itertools

# using zip_longest() to combine two iterables.
print ("The combined values of iterables is : ")
print (*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue ='_' )))
