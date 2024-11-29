#first create one string
str="I am a coder."

#ends with function
str="I am a coder."
print(str.endswith("er.")) #returns true if string ends with substr
print(str.endswith("am")) #returns false value

#capitalize function
str="i am a coder."
print(str.capitalize())
print(str)

#replace function
str="i am a coder."
print(str.replace("coder","student"))

#find function
str="i am a coder." 
print(str.find("am")) #finds on which index the character is

#count function
str="I am am a codeeerrr."
print(str.count("e")) #count how much time the character exists

str="fjdv$$$hgg$$hgcvjg"
print(str.count("$"))

def addnum():
 fnum = int(input("Enter first number: "))
 snum = int(input("Enter second number: "))
 sum = fnum + snum
 print("The sum of ",fnum,"and ",snum,"is ",sum)

addnum()