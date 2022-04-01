def f2(a,b,c):
   """This is a function which will determine the grades"""
   avg = (a+b+c)/3
   Grade = ("A" if avg > 80 else ("B" if avg > 60 else "C"))
   print("avg is ",avg)
   print("Grade is ",Grade)
#    #return avg
# r = f2(98,66,79)
# print(r)
f2(98,66,79)
print(f2.__doc__)
