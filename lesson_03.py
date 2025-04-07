# slicing 
name = "xani";
# string is immutable , we can not do customiszation on character level after creating a string

nameShort = name[0:3] #start form index 0 to 3 excluding 3 which is "xan"
print(nameShort);

anotherName =name[1:3]
print(anotherName);

# negative/ reverse slicing

choosenName = "harry"
# userName =choosenName[-4:-2]
# print(userName);
 
print(choosenName[-4:-1]) # arr
print(choosenName[1:4])   # arr

print(choosenName[:4]) # is same as print(choosenName[0:4])
print(choosenName[1:]) # is same as print(choosenName[1:5])
print(choosenName[1:5]) 
# all have same output arry 

# slicing with skiping values 
# we can provide a skip value as a part of slice 
# usualy called start stop step values

print("==================new area======")

word = "amazing"
print(word[1:6:2]) # start at index 1 stop at index 6 and skip/keep step of 2 

characterName = "spiderman"
print(characterName[2:6:2])

# fnctions of string
print("==================functions of strings====")
srt="xani"

print(len(srt)); # 4

print(name.endswith("ni"))# ture 

print(name.startswith("xa")) # startswith & ends with these functions are case sensiteive 
#if XA or NI was used then outcome will be false

print(name.capitalize()) # only capitalize the first character in the string

print(name.upper())

print("CAN".lower())

a= "programing in \"python\" is \n simple \n and fun"
print(a) #\n is used for line break or enter in a print sequence
# and \"(word)\" is used for applying "" in a print secquence 