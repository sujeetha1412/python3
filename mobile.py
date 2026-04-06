d={}
n=int(input("enter number of records:"))
for i in range(n):
   num=input("Enter mobile number:")
   name=input("Enter name:")
   d[num]=name
s=input("enter number to search:")
if s in d:
   print("name:",d[s])
else:
   print("number not found")
