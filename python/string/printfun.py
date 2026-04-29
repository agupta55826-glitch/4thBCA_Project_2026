'''print multiple items
name="akash"
age=20
str=name
print("name is", name,"and age", age, "years old!")
print(str)

print("apple","mango","cherry","banana","grapes",sep=" , ")

print("Hello Akash",end=" ")
print("How are you???")

input function

user_input=input("please enter something:")
print("you entered:",user_input)

for integer input

age=int(input("please enter your age:"))
print("you are",age,"years old.and after 5 years you will be",age+5,"years old.")

for float input

height=float(input("enter your height in meters:"))
print("your height is",height,"meters")

# comperision operator

print(10>5)
a=10
b=20
print("Equal to",a==b)
print("10"==10)
print("not equal to",a!=b)
print('greater than',a>=b)

number=int(input("Enter your number:"))
if(number>0):
    print("number is greater")
if(number<0):
    print("number is less") 
else:
    print("invalid number") 

num=int(input("enter your number: "))
if num%2==0:
    print("this number is even number")
else:
    print("this is odd number")   

num = int(input("Enter your number: "))
if num>0:
    print(" this is +ve number")
elif num<0:
    print(" this is -ve number")
else:
    print("this number is == 0")   '''       
