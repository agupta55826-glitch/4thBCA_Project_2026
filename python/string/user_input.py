'''User = int(input("enter your first number: "))
user2=int(input("enter your second number: "))

add = User+user2
print("total number is:", add)'''

'''num= int(input("enter your first number: "))


if num%2 == 0:
    print("this is even no.")
else:
    print("this is odd no.") '''   

#+ve,-ve,0number check

'''num= int(input("Enter your number:"))

if (num>0):
    print("this is positive no.")
elif (num<0):
    print("this is negative no.")
else:
    print("this number is zero")        

    # find out the indexing values
'''
'''list=[29,30,10,23,40,59,39,29,54,76,54]
target=int(input("Enter element to search: "))
if target in list:
    print(list.index(target))
else:
    print("out of range")    '''

# find out the indexing values second method
lst=[2,4,5,7,9,6]
target=int(input("enter element to search: "))
try:
    print(lst.index(target))
except ValueError:
    print("out of range")    