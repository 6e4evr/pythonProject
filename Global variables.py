k = 20 ##### GLOBAL VARIABLE COZ ITS OUT OF BLOCK OF CODE
def f1():
   # k = 33#############LOCAL VARIABLE COZ ITS INSIDE THE BLOCK OF CODE HENCE THE NAME "LOCAL"
    m = 21
    s = k+m
    print(s)
f1()
print("************************************************************")
# **********IN THE PRESENCE OF LOCAL VARIABLE THE PROGRAM DOESNT CONSIDER THE GLOBAL VARIABLE***************
k = 20 ##### GLOBAL VARIABLE COZ ITS OUT OF BLOCK OF CODE
def f1():
    k = 33#############LOCAL VARIABLE COZ ITS INSIDE THE BLOCK OF CODE HENCE THE NAME "LOCAL".
    m = 21
    s = k+m
    print(s)
f1()
print("************************************************************")
def f1(s):
    print(s,"THANK YOU , VISIT AGAIN!!!!!!!!!!")
f1("WELCOME TO OUR HOTEL\n")##### this statement will be displayed first followed by the above statement
######## THE ABOVE PROGRAM CAN BE USED TO MAKE TEMPLATES LIKE IN INVOICES, TOKENS,ETC
print("************************************************8")
k = 22
def f1():
    m = 33
    global k # in the absence of a local variable we can modify the global variable by declaring it within the function code.
    k = k + 44
    s = k + m
    print(s)
f1()
print("*****************************************************")

x = 77
def f1():
    x = 22
    def f2():
        global x
        x = 90
    #print("value of x before calling f2 is",x)
    f2()
    print("value of x after calling f2", x)
f1()
print(x)

print("*********************************************")

x = 77
def f1():
    x = 22
    def f2():
        global x
        x = 90
    print("value of x before calling f2 is",x)
    f2()
    print("value of x after calling f2", x)
f1()
print(x)
