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

# [for loops in else]:
 
listItem = [11,22,33]

for i in listItem:
    print(i)
else:
    print("done")

# [ BREAK , CONTIBUE OR PASS IN LOOPS ]

# break
for i in range(100) :
    if(i == 34):
        break # exit the loop
    print(i)

# continue 

for i in  range(50):
    if(i == 35):
        continue # Skip this iteration right now 
    print(i)
# it skiped 35 and continued 

# pass

for i in range(30):
    pass
    # it prevents errors cause the satement is incomplete
i= 0 
while(i<5):
    print(i)
    i=i+1

print("========= practice set ==========")

# Q [ write a program to print multiplication table of a given number using for loop. ]

n = int(input("enter a number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}");

# Q [write a program to great all the person name stored in a list 'l' and which start with s. ]
l= ["harry" , "shoan" , "sachin" ,"rahul"]

for name in l:
    if(name.startswith("s")):
        print(f"hello {name}");


# Q [ write a program to print multiplication table of a given number using while loop. ]

n = int(input("enter a num: "))

i = 1
while(i<11):
    print(n*i)
    i = i+1;

# find if the number is prime of not 
n = int(input("enter a number: "))

for i in range(2,n):
    if(n%i) == 0:
        print("number is not prime")
        break
else:
    print("number is prime")
