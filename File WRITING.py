# f = open("cricket.txt","w")
# f.write("khulla is a good bowler")
# f.close()

###############################################
f = open("cricket.txt","a")
a = f.write("khulla is a good bowler\n")##prints number of characters written
print(a)##prints number of characters written
f.close()