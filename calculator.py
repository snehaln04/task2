print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num = int(input(" enter your choice : "))

a = int(input("enter first number : " ))
b = int(input("enter second number : " ))

if(num==1):
   print("addition is : ", a+b)

elif(num==2):  
  print("substraction is : ", a-b)

elif(num==3):  
  print(" multiplication is : ", a*b)

elif(num==4):
  print(" division is : ", a/b)

else:
  print("invaid operation")
