# Loops → Repeat actions while a condition is true.
# for while → Repeat a block of code while a condition is true.


# we can also define range like this range(5, 10) # This will give us numbers from 5 to 9
for i in range(3):
    print("Hello")  # Prints 3 times

# while loop example
count = 0
while count < 3:
    print("Hello")
    count += 1  # Increment count to avoid infinite loop        

# -----------------------------------------------------------------------------------------------
'''
Control Statements → Change loop behavior.
break → Stop loop
continue → Skip to next iteration
'''

for i in range(5):
    if i == 3:
        break
    print(i)  # Stops when i = 3
for i in range(5):
    if i == 3:
        continue
    print(i)  # Skips printing when i = 3   

# -----------------------------------------------------------------------------------------------


# Manoj Test

i = ["Amisha", "Manoj", "Ravi", "Shubham", "Ankit", "Priya", "Rahul", "Neha", "Suman", "Rohan"]
for i in i:
    print(i, "is friend of Manoj's")

# -----------------------------------------------------------------------------------------------

count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment count to avoid infinite loop


# -----------------------------------------------------------------------------------------------

# Example of using continue and break statement

list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

for i in list:
    if i == 4:
        continue
    elif i == 7:
        break
    else:
        print(i)


# Manoj Test 

# Question # Print Even Number till 50

for i in range(50):
    if i%2 == 0:
        print(i, end=" ")