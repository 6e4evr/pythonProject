d2= {}
d1 = { "Akshita" : "pizza",
       "satyajeet" : "Idly",
       "Mom" : "Moong",
       "Bhai" : "Mutton",
       "Duggu" : {"B" : "Bread", "L" : "roti", "D" : "Rice"}
       }
print(d1)
print(d1["satyajeet"])
print(d1["Duggu"])
print(d1["Duggu"]["D"])
print(d1.keys())#returns keys
print(d1.values())#returns values
d1["Utsav"] = "Dosa"
print(d1)
del d1["Utsav"]#deletes a key value pair
print(d1)
d2 = d1.copy()#makes a copy of dictionary
print(d2)
del d2["satyajeet"]
print(d2)#after deleting "satyajeet" d2 is affected but d1 remains unaffected
print(d1)
d1["satyajeet"] = "MB"#changing the value of satyajeet from idly to MB
print(d1)