'''
DataStre Is a way of Organizing and storing data in a computer so that it can be accessed and modified efficiently.
Data structures are essential for managing large amounts of data and enabling efficient algorithms.
Common data structures include arrays, linked lists, stacks, queues, trees, and graphs.
Each data structure has its own strengths and weaknesses, and the choice of data structure can significantly affect the performance of an algorithm.
'''
# Data Structures Overview
# Lists are a basic data structure that allows for the storage of a collection of items.
# In Python, lists are dynamic arrays that can grow and shrink in size, allowing for efficient
# insertion and deletion of elements. Lists can store items of different data types, including other lists
# Example:
my_list = [1, 2, 3, 'four', [5, 6]]
print(type(my_list))  # Output: <class 'list'>
print(my_list)  # Output: [1, 2, 3, 'four', [5, 6]]
print(my_list[3])  # Output: 'four'
# Lists can be manipulated using various methods such as append, remove, and sort.
my_list.append("Manoj")
print(my_list)  # Output: [1, 2, 3, 'four', [5, 6], 'Manoj']

my_list.remove(3)
print(my_list)  # Output: [1, 3, 'four', [5

my_list.sort()  # This will raise an error because 'four' and [5, 6] are not comparable
print(my_list)  # Output: [1, 2, 'four', [5, 6], 'Manoj']