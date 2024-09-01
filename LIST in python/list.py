thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
tropical = ["mango", "pineapple", "papaya"]

# Accessing list
print(thislist[1])
print(thislist[-4])

# Append in list
thislist.append("beetroot")
print(thislist)

# Inserting in list with index number
thislist.insert(1, "khoya")
print(thislist)

# Extend list (merge two list)

thislist.extend(tropical)
print(thislist)

# Removing a list

thislist.remove("banana")
print(thislist)  #or 
thislist.pop(1)  #pop method is also used to remove items by specifying index number 
print(thislist)

# deleting keyword

del thislist[0] #you can use del keyword also to remove a item in a list or to remove a list
print(thislist) 

#clear keyword 
thislist.clear()
print(thislist)  #this key word is used to empty the list 




