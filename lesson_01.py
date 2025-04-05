#  variables
a = 1
b = 3
print(a+b)
# veriables works as containers

# datatypes

a = 1  # here a is an integer
b = 5.334  # here b is float

c = "xani"  # c is string
d = False  # boolean datatype

e = 'None'  # is a none type veriable

# false and none are diff/.....
# @is not used in python cause of some internal functions

# here is an example for if and else conditions
if 1 == 1:
    print("true");

else:
    print("false");

# increment , decrement operators

a = 50;
b = 50;
c=a+b;
print("here is you ans:",c);

# assignment operators

a=4-2
b=6
b +=3 #INCREMENT OPPERATOR the value of b by 3 and assign it to b
print(a);
print(b);
print(a+b) # that means it increases it and then add both the variables
b -=3; # DECREMENT OPPRATOR 
print(b);# now cause the previous line is active and decrement opperator is used , then the ans is 6 , cause it was increased by 3 

b *=3;
print(b); #18 cause 6 x 3 

b /=3;
print(b); #6 cause it was 18 first 

# comparison opperators .... they always ans in boolean value
 
#example

z= 5>=4
print(z) #true 

if 5>8:
    print("true");
else:
    print("False");
#false 

#loggical operators

t= True or False
print(t);
#truth table with "or"
print("true or false is:", True or False)
print("true or true is:",True or False)
print("false or ture is:", True or False)
print("false or false is:", True or False)

#truth table with and 
print("true or false is:", True and False)
print("true or true is:",True and False)
print("false or ture is:", True and False)
print("false or false is:", True and False)

# not works as vice versa for the operators
print(not(False));
print(not(True));