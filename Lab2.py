print('hello world')
text1='Bonjour'
text2='Montreal'
res=text1 + " " + text2
print(res)
text3='montreal'
uppercase=text3.upper()
print(uppercase)
text4='MONTREAL'
lowercase=text4.lower()
print(lowercase)
age=int ( input ("Enter your age:"))

if age >= 65:
   print('You are a senior citizen')

elif age >= 18:
    print('You are an adult')

else:
    print('You are a minor')

