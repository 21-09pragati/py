# defalult read mode.

# f= open("pooja.txt","r") ........................not creating new file ,required created file to open.
# content=f.read(15)
# print(content)
# f.close()
# # print(type(f))
# # print(type(content))

#write mode.

# file =open("pooja2.txt", "w") ..................new file created and write.
# file.write("This is good practice./n")
# file.close()

# append write mode

# file =open("pooja1.txt","a")  ---------------new file create and write.
# file.write("This is new file")
# file.close()
 
#  read and write mode.
 
# file =open("pooja.txt","r+")    
# content=file.read()
# print(content)      
# file.write("this is read write mode") 
# c=file.write("this is read write mode") 
# content=file.read()
# print(content)
# file.close()


# write and read mode.

# f=open("pooja2.txt","w+")
# f.write("hi welcome to write and read mode ")
# content=f.read()
# print(content)
# f.close()

# seek and file functions in file handling.


# file=open("pooja.txt","rt")
# print(file.tell())
# print(file.readline())
# print(file.tell())
# file.seek(0)
# print(file.readline())
# file.close()



# using with block 

# with open("pooja.txt","a") as f:
#     a=f.write("hi how are you\n")
#     print(a)

# with open("pooja.txt") as file:
#     a=file.readline()
#     prhttps://www.youtube.com/watch?v=xTmBq-CQTVU&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=24&pp=iAQBint(a)
#     print(file.readline())  
#     print(file.readline())  