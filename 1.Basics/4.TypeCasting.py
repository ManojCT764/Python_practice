'''
-> The Process of changing Data Type of a variable is called Type Casting.
Types
    int() → to integer
    float() → to decimal
    str() → to string
    bool() → to boolean (True or False)
    list() → to list
    tuple() → to tuple
    set() → to set
    
    dict() → to dictionary
    complex() → to complex number
    bytes() → to bytes
    bytearray() → to bytearray
    memoryview() → to memoryview
    frozenset() → to frozenset
    range() → to range
    None → to NoneType
'''     

# Integer to float
a = 5
b = float(a)
print(b)         # 5.0

# Float to integer
x = 3.8
y = int(x)
print(y)         # 3

# Number to string
num = 42
text = str(num)
print(text)      # "42"

# String to integer
s = "100"
n = int(s)
print(n)         # 100

# String to float
f = float("3.14")
print(f)         # 3.14

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3)

# Tuple to set
my_set = set(my_tuple)
print(my_set)    # {1, 2, 3}

# Bool casting
print(bool(0))   # False
print(bool(5))   # True
print(bool(""))  # False
