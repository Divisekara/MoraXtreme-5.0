
##Input matrices change the matrices as wish
L=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
M=[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

## Operation is L * M  first matrix is and second matrix is M

L_rows, L_cols = len(L), len(L[0])
M_rows, M_cols = len(M), len(M[0])

#In order to multiplication be validate L_cols == M_rows
##Output matrix size is L

#print(L_rows, L_cols)

result = []

for i in range(0, L_rows):
    temp_row = []
    
    for j in range(0, M_cols):
        x=0
        
        for k in range(0, L_cols):
            x += L[i][k] * M[k][j]
            
        temp_row.append(x)

    result.append(temp_row)
     
print(result)




