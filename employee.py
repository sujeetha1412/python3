employees=((101,"ravi",45000),(102,"sita",60000),(103,"arun",75000),(104,"meena",50000))
print("employee details:")
for emp in employees:
   print("id:",emp[0],"name:",emp[1],"salary:",emp[2])
search_id=int(input("enter employee id to search:"))
found=False
for emp in employees:
   if emp[0]==search_id:
      print("employee found:")
      print("id:",emp[0],"name:",emp[1],"salary:",emp[2])
      found=True
      break
if not found:
   print("employee not found")
highest=employees[0]
for emp in employees:
   if emp[2]>highest[2]:
      highest=emp
print("employee with highest salary:")
print("id:",highest[0],"name:",highest[1],"salary:",highest[2])
print("\nemployee with salary greater than 50000:")
for emp in employees:
   if emp[2]>50000:
      print("id:",emp[0],"name:",emp[1],"salary:",emp[2])
