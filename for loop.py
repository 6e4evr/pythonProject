##l1 = ["sam","axis","max","pam"]
#for i in l1:
#    print(i)
l1 = [["sam",10],["axis",20],["max",30],["pam",40]]
for i,age in l1:
    print(i,age)
candidate = input("enter the name ")
if age > 20:
    print("elder")
elif age == 10:
    print("equal")
else:
    print("younger")
