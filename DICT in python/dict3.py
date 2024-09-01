thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Removing item
#pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)

#popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)


#del keyword removes the item with the specified key name and used to delete the whole dictionary also

del thisdict["model"]
print(thisdict)