l1=[1,2,3]
l2=[10,20,30]
while True:
   print("\n1.insert at position")
   print("2.append element")
   print("3.compare limits")
   print("4.print id of element")
   print("5.find first occurence")
   print("6.exit")
   c=int(input("enter choice:"))
   if c==1:
      pos=int(input("position:"))
      val=int(input("value:"))
      l1.insert(pos,val)
      print(l1)
   elif c==2:
      val=int(input("enter element:"))
      l1.append(val)
      print(l1)
   elif c==3:
      if l1==l2:
               print("both lists are equal")
      else:
               print("lists are not equal")
   elif c==4:
      for i in l1:
               print(i,"ID",id(i))
   elif c==5:
      x=int(input("enter element to search:"))
      if x in l1:
               print("index",l1.index(x))
      else:
               print("not found")
   elif c==6:
      break
   else:
      print("invalid choice")
