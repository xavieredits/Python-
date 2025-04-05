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