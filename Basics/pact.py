# dict1={'adatya':22,'vinodh':22,'tarachand':44};
# dict2={'aysh':23 , 'akash':45 , 'suraj':77};
# # dict1.update(dict2)
# # print(dict1);
# dict1['ayush']=99
# print(dict1);

# for num in range(5):
#     if num < 0:
#         print(num*10);

# num = int(input(entery:))
# if num %2 == 0:
#     print("even");
# else:
#     print("odd");

rows = int(input("Enter number of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("* ",end="")
    print()

