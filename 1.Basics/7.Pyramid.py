#----------------------------------------------------------------
# Pyramid Pattern using while loops
a = 0

while a < 5:
    b = 0
    while b <= a :
        print(" * ", end="")
        b += 1
    print()
    a += 1
    
#-----------------------------------------------------------------
# Pyramind Pattern using both for and while loops
y = 0
for x in range(0, 5):
    while y < x:
        print(" * " * x)  # Prints asterisks in a pyramid shape
        y += 1
        break

#-----------------------------------------------------------------
# Pyramid Pattern using for loops

for f in range(5):
    for e in range(f + 1):
        print(" * " , end="")
    print()  # Moves to the next line after each row

#------------------------------------------------------------------

for q in range(5):
    for r in range(5):
        print(" # ", end="")
    print()

# outer loop defines columns
# inner loop defines rows