in_put=input("Input: ")

list_1=["a","e","i","o","u"]
list_2=["A","E","I","O","U"]

for char in list_1:
   if in_put.find(char)>=0:
       in_put=in_put.replace(char,"")


for char_2 in list_2:
   if in_put.find(char_2)>=0:
       in_put=in_put.replace(char_2,"")

print("Output: "+in_put)