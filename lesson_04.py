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
