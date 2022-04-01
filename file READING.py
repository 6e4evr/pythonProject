# f = open("cricket.txt","rt")
# content = f.read(3)
# print(content)
# f.close()
##############################################################
f = open("cricket.txt","rt")
for line in f:
    print(line,end=" ")
###################
# f = open("cricket.txt","rt")
# print(f.readline())#reads line wise*********READLINE************
# print(f.readline())
# print(f.readline())
# print(f.readline())
########################################################
f = open("cricket.txt","rt")
print(f.readlines())#stores lines in the "LIST"***********READLINES***********


