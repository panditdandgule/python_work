"""
|>>> c = Counter('abcdeabcdabcaba')  # count elements from a string
|
|  >>> c.most_common(3)                # three most common elements
|  [('a', 5), ('b', 4), ('c', 3)]
|  >>> sorted(c)                       # list all unique elements
|  ['a', 'b', 'c', 'd', 'e']
|  >>> ''.join(sorted(c.elements()))   # list elements with repetitions
|  'aaaaabbbbcccdde'
|  >>> sum(c.values())                 # total of all counts
|  15
|
|  >>> c['a']                          # count of letter 'a'
|  5
|>>>for elem in 'shazam':           # update counts from an iterable
|      c[elem] += 1                # by adding 1 to each element's count
"""

"""
|  >>> c['a']                          # now there are seven 'a'
|  7
|  >>> del c['b']                      # remove all 'b'
|  >>> c['b']                          # now there are zero 'b'
|  0
|
|  >>> d = Counter('simsalabim')       # make another counter
|  >>> c.update(d)                     # add in the second counter
|  >>> c['a']                          # now there are nine 'a'
|  9
|
|  >>> c.clear()                       # empty the counter
|  >>> c
|  Counter()
"""