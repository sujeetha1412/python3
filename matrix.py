mat={}
print("enter values for matrix :")
A=[]
for i in range(2):
   row=[]
   for j in range(2):
      row.append(int(input("enter number:")))
      A.append(row)
print("enter values for matrix :")
B=[]
for i in range(2):
   row=[]
   for j in range(2):
      row.append(int(input("enter number:")))
      B.append(row)
C=[[0,0],[0,0]]
for i in range(2):
   for j in range(2):
      C[i][j]=A[i][0]*B[0][j]+A[i][1]*B[i][j]
print("result matrix:")
for row in C:
   print(row)
