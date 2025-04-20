p1 ="make money online"
p2 ="buy now"
p3 = "bank loan"

msg = input("enter you msg:")
# now we use "in" , "or" prase to detect something present in the data
if((p1 in msg) or (p2 in msg) or(p3 in msg)):
    print("spam");
else:
    print("working on it");
