#16/7/24



'''
#VARIABLES

name="Pragati"
print(name)

place=input("Enter Place name: ")
print(place)

#DATA TYPES

a=12
b=1.2
c="Pragati"
d=True
print("Type of a: ",type(a))
print("Type of b:",type(b))
print("Type of c:",type(c))
print("Type of d:",type(d))

#CONCATE VARIABLE IN STRING
year=2023
name="Pragati"
university="Shivaji University"

st1=name + ' is passout in '+ str(year) + ' from ' + university + ' ' 
print(st1) 

#TYPECASTING

p=int(1.2)
q=float(11)
r=str(12)
ss=float("99")
s=float("23.4")
t=str(22)
u=str(22.4)
v=int("3")

print([p,q,r,s,t,u,v])'''

#JULY_18
'''
a=6
b=2
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)'''

#Strings and slicing

msg="Hello Welcome it\'s to VS Code"
'''print(msg + msg)#no space between two string after concatenate
print(msg,msg)#space between two strings seperating by comma

print(msg.upper())

print(msg.capitalize())

print(msg.lower())

print(msg.)

print(msg.title())

print(len(msg))

print(msg.count('e'))

print(msg[1:5])

print(msg[::-1])

print(msg[-1:-4])'''

'''msg="Welcome to Python 101: Strings"

#1 Welcome Ring To Tyler
msg1=msg[18]+' '+msg[0:7]+' '+msg[25:30]+ ' '+msg[8:10]+' '+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())
print(msg1[::-1])'''

#multiline string
msg2="""Hello,I am pragati Patil.
I am from Karad.
I have completed Btech in CSE"""
print(msg2)