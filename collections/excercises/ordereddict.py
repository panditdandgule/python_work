from collections import OrderedDict

newdict=OrderedDict([('color1', 'Red'), ('color2', 'Green'), ('color3', 'Blue')])
print("Original Dict: ",newdict)

newdict.update({'color0':'White'})

newdict.move_to_end('color0',False)

print(newdict)