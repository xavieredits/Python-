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

for i in range(1,4,2):
    print(i,"hello")
#  use of start , stop and step can be applied

anotherList = [1,4,66 , "shubh" ,"can" , "english"]

for j in anotherList:
    print(j);

# for loops with tuples 

t = ( 1 , 22 ,650 , 54 , 75)

for i in t:
    print(i);

#  ittration of string in loops

a = "luffy"
for i in a:
    print(i)
a = "luffy"
for i in a:
    print(a)
# check for the  diff

