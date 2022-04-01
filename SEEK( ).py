f = open("cricket.txt","rt")
print(f.seek(5))### enables us to read the content from desired character
print(f.tell())#### tells us where the file pointer is at
print(f.readline())#reads first line
print(f.seek(13))
print(f.tell())
print(f.readline())#reads second line
print(f.seek(35))
print(f.tell())
print(f.readline())#reads third line
f.close()