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

print(all_fact())
print(all_fact())
