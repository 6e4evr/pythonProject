n1 = int(input("enter 1st number :"))
n2 = int(input("enter 2nd number :"))
Op = input("enter an operator:")
if input == "45+3":
    print("88")
elif input == "22-11":
    print("99")
elif input == "33*3":
    print("23")
elif input == "110/10":
    print("1")
elif input == "2**5":
    print("12")
elif Op == "+":
    print(n1+n2)
elif Op == "-":
    print(n2-n1)
elif Op == "*":
    print(n1*n2)
elif Op == "/":
    print(n2/n1)
elif Op == "**":
    print(n1**n2)
else:
    print("error: ")