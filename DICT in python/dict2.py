thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# changing the value of key
thisdict["year"] = 2018  #used to add new items and change item both
print(thisdict)

#update() method will update the dictionary with the items from the given argument
thisdict.update({"year": 2020}) 
print(thisdict) #used to add new items if item is not present