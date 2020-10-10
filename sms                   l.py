A = input().strip().upper()
B = input().strip().upper()

n = len(A)
m = len(B)

an=0
for i in range(0,m):
    L = A[i:n-m+1+i]
    x=B[i]
    if (x!="["):
        an += L.count(x)
    
print(an)
