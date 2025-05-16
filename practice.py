x=10
if x>5:
   print("x is greater than 5")

a=13
if a>15:
   print("a is greater than 15")
elif a>5:
    print('a is greater than 5')
else:
   print('a is not greater than 5')

b=3
if b>5:
   print('b is greater than 5')
else:
   print('b is not greater than 5')


fruits=['apple','banana','cherry']
for fruit in fruits:
   print(fruit)

numbers=[1,5,7,9]
for number in numbers:
   print(number)

num_input=int(input("Enter how many numbers:"))
numbers=[]

for i in range(num_input):
   while True:
    try:
        num=float (input(f"Enter numbers {i+1}:"))
        numbers.append(num)
        break
    except ValueError:
       print("Invalid Input.Please Enter a Number")

print("Entered Numbers:",numbers)

   
