s = set()
l = [1,2,3,4,5]
s1 = set(l)#converts list into set
print(s1)
print(max(s1))#returns maximum value
print(min(s1))#returns minimum value
print(len(s1))#returns number of elements in a  set
s1.add(6)#adds 6 in the set
print(s1)
l1 = [5,6,7,8]
s = set(l1)#converts list into set
s.remove(5)#removes 5 from set s
s.remove(6)
s.add(5)
s.add(6)
print(s)
print(s1.isdisjoint(s))# returns true if both the sets are disjoint else false
print(s1.intersection(s))#returns only common elements from both sets
print(s1.union(s))#returns all the values in both sets by clubbing them into one set
###########A SET ONLY STORES UNIQUE VALUES ONLY##########
