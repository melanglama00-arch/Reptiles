print("learning about the strings. \n also string features")
str3="apnecollege"
print(len(str3))


#string concatination
str0="Milan"
str1="juk"
str2="Lama"
finalstr=str0 + str1 + str2
print(finalstr)
print(len(finalstr))

#slicing in python
print("the example of slicing of string in python")
str4="welcometojungle"
print(str4)
print(str4[2:13])
print(str4[3:4])
print(str4[6:10])

#calculate the greatest among 3 numders asking the numders from users
print("Enter the numbers accordingly")
a= int(input("Enter a num: "))
b= int(input("Enter b num: "))
c= int(input("Enter c num: "))

#using the if conditional statement
if(b<a>c):  
    print("the gratest number is a: ",a)
elif(a<b>c): 
   print("the gratest number is b: ",b)
elif(a<c>b): 
   print("the gratest number is c: ",c)
else: 
    print("in valid numbers")

#the concept of list in python 
info= ["milan", 20, "nepal", "happy"]
print(info)
print(info[3])
#tuples in python
print("tuple is bult-in datatype.That is immutable")
tup= (34,45,66,77)
print(tup[2])
print(type(tup))
print(tup[1])

   



