'''from the string "Welcome to python 101 : Strings" etract text and create/print
a new string that says
1 Welcome ring to Tyer  
Every first letter should be capitrilized.
print the same string backword'''


str = "welcome to python 101: Strings"
ptr= (str[18].capitalize()+' '+str[:7].capitalize()+' '+str[25:29].capitalize()+' '+str[8:10].capitalize()+' '+str[8].capitalize()+str[12]+str[6]+str[25])
print(ptr)
print(ptr[::-1])