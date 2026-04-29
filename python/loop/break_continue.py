'''i=1
while i<=10:
    print(i)
    if i==7:
        break
    i+=1
    print('hii')'''
'''
numbers=[1,2,3,4,5,6,7]
for i in numbers:
    print(i)
    if i==3:
        print("Found 3,breaking")
        break'''
        

        #continue

'''i=1
while i<=10:
    if i==8:
        i+=1
        continue
    print(i)
    i+=1 '''

# easy way

'''i=1
while i<=10:
    # print(i)
    # i+=1
    if i!=8:
        print(i)
    i+=1

'''
    # pass(like placeholder)

# for i in range(1,6):
#     if i==3:
#         pass
#     else:
#         print(i)


while True:
    user_input=input("Enter number:")
    if user_input=="q":
        break
    elif user_input.isdigit():
        print("valid number")
    else:
        pass    

