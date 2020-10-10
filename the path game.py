n,k = list(map(int, input().strip().split(" ")))
L = input().strip()

answer=[]

count = 0
while(count<n):
    for i in range(1,k+1):
        if(L[count+i]=1):
            

print(" ".join(answer))
