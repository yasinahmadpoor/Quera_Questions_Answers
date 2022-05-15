adad = int(input())
list = []
for x in range(1,adad):
 baqi = adad % x
 if baqi == 0:
   list.append(x)
sum_list = sum(list)
if adad == sum_list:
  print("YES")
else:
  print("NO")

        

           
 

  
  

