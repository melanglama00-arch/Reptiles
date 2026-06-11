#practising the filr input/output in python
#opening and reading the file text
f = open("sample.txt","r")
data = f.read()
print(data)
f.close()

#opening and writhin to the file
f = open("demo.txt", "w")
f.write("i am trying my best to be the best version of me")
f.write("\ni would to say best of luck to myself mu coading journy")
f.close()

#the way to write the file i/o with syntax
with open("demo.txt","w") as f:
    f.write("best way to write and read the datas")

#DELETING THE file in python using the module that is os
    import os
    os.remove("demo1.txt")

