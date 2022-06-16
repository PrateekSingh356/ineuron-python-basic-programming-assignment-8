#3. Write a Python Program to Transpose a Matrix?
A = [[12, 7],
     [4, 5],
     [7, 8]]
B = [[0, 0, 0],
     [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        B[j][i] = A[i][j]
for i in range((len(A))):
    for j in range(len(A[0])):
        A[i][j] = B[j][i]
print(B)
