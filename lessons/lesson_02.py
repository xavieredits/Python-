#  finding type of variables
a = 123
t = type(a);
print(t) #<class.int>

b =1.23
p=type(b);
print(p); #<class 'float'>

c="xani";
o=type(c);
print(o) #<class 'str'>

#==================================
# converting/interchanging functions

x =str(b);
print(type(x),x)# coverted into string

y ="1.32"
print(type(y),y) #string right now but converting to float

k =float(y);
print(type(k),k) #float possible

# ================================================
# ================================================

#creating a simple calculator with user entry

num1= int(input("enter number 1 :"))
num2= int(input("enter number 2 :"))

num3= num1+num2;
print("the sum is :", num3);

# if int is not use in the starting the input is taken as string

# modulous opperator  "%"
a=34
b=5
print(a%b) #4

num1= int(input("enter number 1 :"))
num2= int(input("enter number 2 :"))

print(num1>num2); # True or false

# square in pythone is " ** "


