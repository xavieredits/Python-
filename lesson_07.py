# loops in python
for i in range(1,5):
    print(i)

# while loops 
print("=========while loops=========")
y = 1
while(y<6):
    print(y)
    y+=1

# this block continues to execute until the condition is false 

# Q: write a program to print "xani" 5 times
s = 0
while(s<5):
    print(s,"xani")
    s = s+1

# print elemets of a list using while loop

list1 = [1,"xani" , "github", "sam" ,34 ,88]

e = 0
while(e<len(list1)):  #here the length of list is used for the range in while loop
    print(list1[e])
    e = e+1

# [ for loops ]
