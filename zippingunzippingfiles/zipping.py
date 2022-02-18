from zipfile import *

f= ZipFile("file.zip", 'w', ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.close()
print("Files.zip crated successfully")