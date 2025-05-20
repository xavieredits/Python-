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

# the file which is opend has to closed to access again.

# writing in a file 
Text = "here is a data to insert "
f = open("/workspaces/Python-/lessons/file.txt","w")
# here "w" refers to the Write mode 
f.write(Text)
f.close()

# read lines function 
f = open("/workspaces/Python-/lessons/file.txt")
lines = f.readlines()
print(lines,type(lines))

f.close()

# while loop for the readlines 
f = open("/workspaces/Python-/lessons/file.txt")
line = f.readline
while(line != ""):
    print(line)
    line = f.readline()
f.close()