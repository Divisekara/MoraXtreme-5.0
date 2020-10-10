n = int(input().strip()) #number of digits
a = list(map(int, list(input().strip())))

def fact(num):
    factorial =1
    if num < 0:
       return 1
    elif num == 0 or num==1:
       return 1
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       return factorial

def all_fact(L):
    total = 1
    for i in L:
        total *= fact(i)
    return total


new=[]
for i in range(n):
    b=a[i]
    if(b==4):
        new.extend([3,2,2])
    elif(b==6):
        new.extend([5,3])
    elif(b==8):
        new.extend([7,2,2,2])
    elif(b==9):
        new.extend([7,3,3,2])
    else:
        if(b!=1 and b!=0):
            new.append(b)

new.sort()
new.reverse()



print("".join(list(map(str,new))))






