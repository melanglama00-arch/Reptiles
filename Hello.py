print("hello nepal")
print("hi this is milanjuk lama ")
print("i am learning the python and exploring")
#practising the variables in pythine
print("  ")
print("Variables in python")
name="milanjuk"
sum=10 + 30
age=20
print("sum of the number is: ",sum)
print("my age is: ",age)
print("My name is:",name)
#taking the input from the users

name=input("name: ")
age=int(input("number: "))
price=float(input("price of py: "))

""" the example of conditional statement where the colors of the traffic light is defines"""

light=input("type color: ")

if(light == "red"):  
    print("stop")
elif(light == "yellow"):        
     print("ready")
elif(light == "green"):  
    print("go")
else:   
    print("not valid traffic ligth")

    #single line ternary operator

    food=input("food name: ")
    food="sweet" if food == "cake" else "bitter"
    print(food)
