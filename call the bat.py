n = int(input().strip())

L=[]

s="00"
line_zeros = " ".join([s]*(2*n+3))
if(n%2==0):
    L.append(line_zeros)
    L.append(line_zeros)
if(n%2==1):
    L.append(line_zeros)

numbers = ['',' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9']
for i in range(10,98):
    numbers.append(str(i))
9
for j in range(n//2):
    line_1 = (s+" ")*(n+1-j) + (numbers[n-j]+" ")*(2*j+1) + (s+" ")*(n+1-j) 
    L.append(line_1)
    next_num = j

#############
Z=[]
if(n%2==1): 
    for q in range((n-4)//2):
        temp_3 = numbers[next_num-q+3:next_num+q+4]
        temp_4 = temp_3[:]
        temp_4.reverse()
        line_3 = (s +" ")*((n+3-2*q)//2) +  " ".join(temp_4) +" "   + (numbers[next_num-q+2] + " ") *(n-2-2*q) + " ".join(temp_3)  + " " + (s +" ")*((n+3-2*q)//2)
        Z.append(line_3)
        L.append(line_3)
        
if(n%2==0): ####This is now ok do not change
    for q in range((n-6)//2):
        temp_3 = numbers[next_num-q+2:next_num+q+3]
        temp_4 = temp_3[:]
        temp_4.reverse()
        line_3 = (s +" ")*((n+3-2*q)//2) +  " ".join(temp_4) +" "   + (numbers[next_num-q+1] + " ") *(n-1-2*q) + " ".join(temp_3)  + " " + (s +" ")*((n+3-2*q)//2)
        Z.append(line_3)
        L.append(line_3)
        
############
middle = [" 3  3  3  3  3 "," 3  2  2  2  3 ", " 3  2  1  2  3 ", " 3  2  2  2  3 ", " 3  3  3  3  3 "]
if(n%2==0):
    middle = [" 3  3  3  3  3 "," 3  2  2  2  3 ", " 3  2  1  2  3 ", " 3  2  2  2  3 ", " 3  3  3  3  3 "]
    for k in range(0,5):
        temp = numbers[4:n+3-k]
        temp_2 = temp[:]
        temp_2.reverse()
        line_2 = (s+" ")*k +    " ".join(temp_2)  + " " +middle[k]    + " ".join(temp)    + " "+  (s+" ")*k

        L.append(line_2)
        
if(n%2==1):
    #middle = [" 3  3  3  3  3  3 "," 3  2  2  2  2  3 ", " 3  2  1  1  2  3 ", " 3  2  2  2  2  3 ", " 3  3  3  3  3  3 "]
    for k in range(0,5):
        temp = numbers[4:n+3-k]
        temp_2 = temp[:]
        temp_2.reverse()
        line_2 = (s+" ")*k +    " ".join(temp_2)  + " " +middle[k]    + " ".join(temp)    + " "+  (s+" ")*k

        L.append(line_2)



###########

Z.reverse()
if(n>6):
    for r in range(len(Z)):
        L.append(Z[r])


########
    


M=[]
for j in range(n//2):
    line_1 = (s+" ")*(n+1-j) + (numbers[n-j]+" ")*(2*j+1) + (s+" ")*(n+1-j) 
    M.append(line_1)
M.reverse()
L.extend(M)

    
s="00"
line_zeros = " ".join([s]*(2*n+3))
if(n%2==0):
    L.append(line_zeros)
    L.append(line_zeros)
if(n%2==1):
    L.append(line_zeros)

print("\n".join(L))

    
