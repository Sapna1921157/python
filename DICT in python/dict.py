thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#-------Accessing dictionary--------
x = thisdict["model"]
print(x)
 #----OR---
x = thisdict.get("model")

# get() function will return all the Keys of dictionary
x = thisdict.keys()
print(x)

# values() function will return all the values of dictionary
x = thisdict.values()
print(x)

# items() method will return each item in a dictionary

x = thisdict.items()
print(x)