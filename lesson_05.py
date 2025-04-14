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


