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