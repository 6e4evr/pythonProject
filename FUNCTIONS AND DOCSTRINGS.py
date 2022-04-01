# a = 9
# b = 10
# c = sum((a,b))
# print(c)
def f1(a,b):
    avg = (a+b)/2
    print(avg)
   # return avg # returns avg and stores that in variable "k"
#k = f1(22,24) # stores the value in variable "k"
f1(22,24)
#print(k)

def f1(a,b):
    avg = (a+b)/2
    print(avg)
    return avg
k = f1(22,24)
print(k)

# def f2():
#     print("Hello world")
# f2()
def f2(a,b,c):
   avg = (a+b+c)/3
   Grade = ("A" if avg > 80 else ("B" if avg > 60 else "C"))
   print(avg)
   print(Grade)
#    #return avg
# r = f2(98,66,79)
# print(r)
f2(98,66,79)