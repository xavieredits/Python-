# File I/O 
'''
a = "a very long string with emails"

emails =[]
3 seconds 
''' 
#  here the file system comes in play, it help the executed file to store the file into the non volatile memory 

f = open("/workspaces/Python-/lessons/file.txt")
# here the path of the file has to be mentioned 
data = f.read()
print(data)
f.close()


