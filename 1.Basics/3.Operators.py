'''
Arithmatic Operators
    + - * / % ** //
'''
a, b = 10, 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3

'''
Comparission Operators
    == != > < >= <=
'''
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

'''
Logical Operators
    and or not
'''
x, y = True, False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

'''
Bitwise Operators
    & | ^ ~ << >>
'''
p, q = 5, 3  # 5 = 0101, 3 = 0011
v = bin(10)
print(v)
print(p & q)   # 1   (0001)
print(p | q)   # 7   (0111)
print(p ^ q)   # 6   (0110)
print(~p)      # -6  (two’s complement)
print(p << 1)  # 10  (1010) Left Shift Operator
print(p >> 1)  # 2   (0010) Right Shift Operator  

'''
Assignment Operators
    = += -= *= /= %= **= //=
'''
z = 5
z += 2   # 7
z -= 1   # 6
z *= 3   # 18
z /= 2   # 9.0
z %= 4   # 1.0
z **= 3  # 1.0
z //= 2  # 0.0
print(z)

'''
Membership Operators
    in not in
'''
nums = [1, 2, 3]
print(2 in nums)     # True
print(5 not in nums) # True

'''
Identity Operators
    is is not
'''
a = [1, 2]
b = a
c = [1, 2]
print(a is b)     # True  (same object)
print(a is c)     # False (different objects)
print(a is not c) # True


# While execuiting python follows Boadmas Rule 
# You can see in the output of the bellow examle both will through a different output
print(4 - (5+2))
print((5+2) - 4)

