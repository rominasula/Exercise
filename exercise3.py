import math
def isPowerOfTwo(num):
    if math.log(num,2).is_integer():
        return True
    else:
        return False
print(isPowerOfTwo(1))
print(isPowerOfTwo(2))
print(isPowerOfTwo(4))
print(isPowerOfTwo(3))