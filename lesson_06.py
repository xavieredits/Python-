# conditionals in python

a = int(input("enter you age:"))
if (a>=18):
    print("you are elligible");
else:
    print("you are underage");

print("end of program");

# [elif]==> it is used in multi condition case

age = int(input("enter you age:"));
if(age>=18):
    print("nice");
elif(age<=0):
    print("invalid")
else:
    print("meh!");

# this is called if elif else ladder ;

#  relation oprators "== ,> , < , >= or <="

#{ multipule if statements in if and else command...}

m = int(input("enter you marks:"))
# if statement number 1
if(m%2==0):
    print("even")
# -- end of if statement number 1 
# if statement number 2
if(m>=18):
    print("selected")
# end of if statement number 2

# here every "if" statement is independent .... bit else and elif is depends on if .. cant stand alone

print("============practice set==========");

a1 =int(input("enter number 1: "))
a2 =int(input("enter number 2: "))
a3 =int(input("enter number 3: "))
a4 =int(input("enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("number is a1",a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greater:",a2)
# etc 


