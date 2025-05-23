# [ FUNCTIONS ANS RECURSIONS ]

# BY creating a function you can define a piece of program to use it again

# FUNCTION DEFINITION
def avg():
    a = int(input("enter value 1: ")) 
    b = int(input("enter value 2: ")) 
    c = int(input("enter value 3: ")) 
    
    average = (a + b + c)/3
    print(average)

avg() # <=== calling the function 

# [FUNCTION WITH ARRGUMNET ]

def goodDay(name , ending):
    print("good day, " + name)
    print(ending)

goodDay("harry" ,"thanks")  # harry goes into the name variable
goodDay("xani" , "great job")


# but : these functions do return a value to which is used to assigning to a new varriable like:

def work(name ,status):
    print("thanks for today " + name)
    print(status)
    return "done"

a = work("neha" ,"loggedin") # here a is getting no value untill you mention return to the funtion
print(a) # <== "done" is returend to the "a"

# [ DEFAULT VALUE ARGUMNET ]

def libWrok(name , status="available"):
    print(f"the book name is {name} and the status is {status}")
    return "thanks for checking"

libWrok("fram" ,"available")
libWrok("comics") # <== here the status is not provided but the default value will be used by the logic

# [ RECURSION ]
# THIS funtion calls itself cause the logic is linked to itself 

# like factoirals 

'''
factorial(0) = 1
factorial(1) = 1
factorail(2) = 1 x 2
factorial(3) = 1 x 2 x 3
factorial(4) = 1 x 2 x 3 x 4
factorial(5) = 1 x 2 x 3 x 4 x 5

factorial(n) = n x n-1 x....... 3 x 2 x 1

factorial(n) = n * factorial(n-1)
'''
# lets build a factorial logic

def factorail(n):
    if( n==1 or n==0):
        return 1
    return n * factorail(n-1)

n = int(input("enter a number to find factoral: "))
print(f"the factorial of the number is : {factorail(n)}")

print("============= practice set ===========")

# write a program using function find greatest of thee number 


def greatestNumber(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c 

a = 1
b = 22
c = 3

print(greatestNumber(a,b,c))

# wite a program using funtion to convert celcius to fahrenhite.
#  [ formula of celcius c/5 = (f-32)/9 ]
# after conversion
#  c = 5*(f-32)/9

def f_to_c(f):
    return 5*(f-32)/9 

f= int(input("enter the temp: "))
c =f_to_c(f)
print(f"{round(c,2)} deg c");  

# wite a function to print first n line fo the pattern (n = 3)

# ***
# **
# *

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)