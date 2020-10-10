##This method is computationally efficient
def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a

def lcm(a,b):
    return (a*b // gcd(a,b))

print(lcm(10,3))




"""
##For this method computationl cost is higher
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print(compute_lcm(num1, num2))

"""
