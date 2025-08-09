'''
Mutable  : Delete/ append/ changesomething         | Example: List 
Imutable : We cant Delete/ append/ changesomething | Example: Touple
'''

# List
# List is just another kind of data container

list_cont = [2, 3.5, 5+6j, True, "Manoj"]
print(list_cont)

# we can access a particular item in the list by doin this
print(list_cont[4])

# we can change the value of a particular item in the list
list_cont[0] = 100
print(list_cont)                

# we can add a new item to the list
list_cont.append("New Item")
print(list_cont)
# we can remove an item from the list
list_cont.remove(3.5)
print(list_cont)
# we can delete an item from the list
del list_cont[2]
print(list_cont)
# we can check the length of the list
print(len(list_cont))
# we can check if an item is in the list
