"""

#Method 1#
import math
print (math.gcd(3,6))

"""

# / real division outputs with the fractional parts
# % stands for remainder division
# // stands for floor division tput is less than or equal to the real value of division

def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a


print (gcd(8,10))




