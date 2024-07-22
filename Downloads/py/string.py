# #Strings and slicing

# msg="Hello Welcome it\'s to VS Code"
# '''print(msg + msg)#no space between two string after concatenate
# print(msg,msg)#space between two strings seperating by comma

# print(msg.upper())

# print(msg.capitalize())

# print(msg.lower())

# print(msg.title())

# print(len(msg))

# print(msg.count('e'))

# print(msg[1:5])

# print(msg[::-1])

# print(msg[-1:-4])'''

# '''msg="Welcome to Python 101: Strings"

# #1 Welcome Ring To Tyler
# msg1=msg[18]+' '+msg[0:7]+' '+msg[25:30]+ ' '+msg[8:10]+' '+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
# print(msg1.title())
# print(msg1[::-1])'''

# multiline string
# msg2="""Hello,I am pragati Patil.
# I am from Karad.
# I have completed Btech in CSE"""
# print(msg2)
# a=2
# b=4
# print('Exponent : ', a ** b)
# n='121'

# if n==n[::-1]:
#     print("Is palindrome")
# else:
#     print("Not palindrome")
















#july 22

#STRING CONCATE USING F string

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# first_name=input("Enter first name: ")
# dist_km=eval(input("Enter distance in km: "))
# mile=float(dist_km)/1.609
# print(f'Hello {first_name.title()}! {dist_km} km is equivalent to {round(mile,2)} miles ')