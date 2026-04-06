d={'Morning':'Evening','Welcome':'Thank you','Hi':'Bye'}
s=input("Enter a sentence:").split(" ")
for i in s:
   if i in d:
      i=d[i]
      print(i,end=' ')
   else:
      print(i,end=' ')
