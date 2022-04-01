str1 = "HELLO SATYAJEET"
print(str1[7])#INDEX
print(str1[0:7]) # string slicing
print(len(str1)) #returns the length of the statement
print(str1[0:66])#will return the output till the end of the statement irrespective of the length defined
print(str1[0:7:2])#will skip two characters and return values
print(str1[0::2])#the blank space is considered as the complete length of the statement and it will return values by skipping two chars
print(str1[:8:2])#blank space is taken as 0
print(str1[:6])#blank space is taken as 0
print(str1[0:9:])#blank space is taken as 1 for skipping
print(str1[::2])#both blank spaces are considered as 0 and cpmplete length respectively
print(str1[::4445])#EXTENDED SLICING
#negative indexing and slicing
print(str1[-9:-2])#will return SATYAJE as the output as S is the -9th index and E is the -3rd index
print(str1[::-1])#will return the reversed string
print(str1[::-2])#will return the reversed string by skipping the 2 chars

