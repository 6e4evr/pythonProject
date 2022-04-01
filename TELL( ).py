# f = open("cricket.txt","rt")# f is a file pointer
# print(f.read())
# print(f.tell())######## returns the line number where the file pointer is at
# f.close()
####################################################################
f = open("cricket.txt","rt")# f is a file pointer
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.close()