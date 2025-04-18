# list and tuples
# lists are mutable , used to store a set of value of any datatype

data = ["akash",20 , "apple",5 ,20.36 , False , "xani"]
print(type(data),data)
# we can do changes in list but not in strings EXAMPLE:

data[0] = "greps";
print(data[0])
print(data)

# methods of lists
# append ==> addtion of a new data in the end 
data.append("harry");
print(data);

# sort ==> for arrangemnt of integers in assending order
list1 = [1,3,45,72,35];
list1.sort();
print(list1);

# reverse ==> descending order
list1.reverse();
print(list1); 

# insert ==> inserting a value in between or at any perticular index of the list

list1.insert(4,"value insert"); # here 4 is the value of index and the next value is what to be inserted 
print(list1);

# pop ==> to remove any data at any perticlar index
list1.pop(2);
print(list1);

# remove ==> to remove a perticular value of list directly without using any index 

list1.remove("value insert");
list1.sort();
print(list1);

# Typles in pythons ==> its a datatype in python which stores immutable sequences of elememts 

x = (1,2,3,4,5,6,7,8,9)
print(type(x));# class => tuple

# tuple is created by the use of "()" bracket and "," with out "," python understand as a single value in "()"

# empty tuple
a=()

# tuple with single value 

a = (1,) #=> tuple with single value 

# create a tuple with multiple objects or elements

y = (1,34,352,235,False,"cani" , "xani" , "amit");

# accessing value of tuple with indexing value 
# y[0] = 234 tuple is immutable so can not change value after creating 

print(y[1]); #value can be accesed  

# methods of tuples

no = y.count(34);
print(no);

i = y.index(235);  # finds  index of the value in the tuple  
print(i);

# repetions in tuples "*"
myTuple=y*3;
print(myTuple);
# (1, 34, 352, 235, False, 'cani', 'xani', 'amit', 1, 34, 352, 235, False, 'cani', 'xani', 'amit', 1, 34, 352, 235, False, 'cani', 'xani', 'amit')

print(len(y));

# slicing in tuples

sliced = y[1:4];
print(sliced); 

# practice set 4 
print("==================== practice set =============")

#  create a program to store seven fruits in a list enterd by a user;

# # my way 

# values = input("enter 7 fruits: ");
# fruits = [values];
# print(fruits);

# pro way 

fruits = []
f1 = input("enter some fruits name:")
fruits.append(f1);
# 0r
# Create an empty list to store the fruits

fruits = []

# Loop to get 7 fruits from the user
for i in range(7):
    fruit = input(f"Enter fruit #{i+1}: ")
    fruits.append(fruit)

# Display the list of fruits
print("\nYou entered the following fruits:")
for fruit in fruits:
    print(f"- {fruit}")