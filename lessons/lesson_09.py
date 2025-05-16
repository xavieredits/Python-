# File I/O 
'''
a = "a very long string with emails"

emails =[]
3 seconds 
''' 
#  here the file system comes in play, it help the executed file to store the file into the non volatile memory 

f = open("file.txt")
data = f.read()
print(data)
f.close()
