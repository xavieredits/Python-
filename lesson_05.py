# Dictionay & sets

marks={
    "maths":34,
    "science":78,
    "hindi":89,
    "english":56
}
print(marks,type(marks));

# soule use of dictonary to use key value pair 

# indextation use in dict
print(marks["english"]);

# properties of python dicts
# unorderd , mutable ,indexed , cannot contain duplicate keys 

# methods of dictonary 

anotherDict ={
    "name":"xani",
    "email":"xani@gmail.com",
    "contact":989070987,
    0:"enpid"
};
print(anotherDict);
# dict items is use to get all the items in key value pair
print(anotherDict.items());

# .keys ==> to get keys from the dict
print(anotherDict.keys());

# .values is uesd to get all the values in the dict

print(anotherDict.values());


# [updating ditonary ]
print(marks);
marks.update({"science":55,"hindi":88});
print(marks);

# [get] ==> returns the value fo the sepecific key(and value is returned)

# note the difference 
print(marks.get('maths'));# returns none;
print(marks["maths"]); # returns error 

# result is same but get returns none when there is no releted element in the dict where as 
# in "[maths]" options it reutruns error in the prompt 

# [ dict.clear() ] ==> it is used to clear all the content in the dictonary 

# sets 
print("================= sets =============== ")

#  set is a colletion of non-reletive elements;
# no repetetion is allowed in sets
# s = {} empty dict

s = {1,3,4,5,6}

e = set() # empty set ==> "()"
print(type(e),e) 
# in set if there is any repeteion of any value example s={1,44,5,3,5,5,5}  , in output it is not diplayed cause it's not included in the set // not repetion //

# sets inclue text and letter vaules too...

G ={1,4,53,4,9,67,"xani"};
print(G,type(G));

# methods of sets 

# [add] ==> is used to add in any set 
s.add(90);
print(s);

# note we can not access values uning index in sets

# what works on sets ==>
# len , remove ,  clear , pop , union , intersection

s.remove(1)
print(s);

print(s.pop() , s) # remove some randome value 

set1 = {1,4,5,6,78}
set2 = {2,56,72,88} 
print(set1.union(set2));

print(set1.intersection(set2));# none of the values intersect

print("============= practice set ============")

# write a program to create a dict and related value extraction

shopList ={
    "milk":56,
    "eggs":29,
    "spices":23,
    "bread":44
};

item =input("enter the intem :")
print(shopList[item]);

#  create a program to enter some number and print unique number from them 

# y =set()
# n = input("enter number1 :")
# y.add(n);
# n = input("enter number1 :")
# y.add(n);
# n = input("enter number1 :")
# y.add(n);
# n = input("enter number1 :")
# y.add(n);
# n = input("enter number1 :")
# y.add(n);
# n = input("enter number1 :")
# y.add(n);
# print(y)

# create an empty dict and add values latter

dic={}
name = input("enter name : ")
marks = int(input("makrs:"))
dic.update({name:marks});
print(dic)