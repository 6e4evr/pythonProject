with open("cricket.txt")as f: ##### works similar to f = open("cricket.txt")
    print(f.read(6))
    print("*******************************")
with open("cricket.txt") as f:
   # print(f.readlines())
   print(f.seek(4))
   print(f.tell())
   print(f.readline())
   print("***************************************")
with open("cricket.txt") as f:
   print(f.readlines())

