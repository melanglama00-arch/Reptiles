#the dictionary and set in python
sub ={
    "math":85,
    "oops":80,
    "english":90,
    "poit":97,
}
print(sub["math"])
print(sub["oops"])
print(sub["poit"])
#methods of dictionary

print(sub.keys())
print(sub.values())
print(sub.items())
print(len(sub))
#type casting the dictionary

print(list(sub.keys()))
print(list(sub.values()))
print(list(sub.items()))

#the sets in python
#the unique collection of the items 

collections = {"tomato", "potato", 2, 4, "world", 34, 55, 38}
print(collections)
print("the lenght of the set collections is",len(collections))

#to creat the empty set in python
letters = set()
veg = {} #this represent dictionary

#to print the datatype or class
print(type(letters))
print(type(veg))

#the methods in sets 
print(collections.add(10))
print(collections)
print(collections.remove(4))
print(collections)
print(collections.pop())

prime = {1, 2, 3, 4, 5, 6, 7}
even = {2, 4, 6, 8}
print(prime.union(even))
print(prime.intersection(even))

#loops in python
fru = ["apple", "banana", "mango", "litchi", "grapes"]
num = [10, 20, 30, 40, 50, 60, 70, 80]

i = 0
while i < len(fru):
    print(fru[i])
    i += 1

for val in range(len(num)):
    if val == 60:
        print("The 60 is found")
        continue

    print(val)

else:
    print("END")
