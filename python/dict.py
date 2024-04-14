mydict = {"name":"zedan" , "age":21 , "city" :"dik"}

print(mydict)


mydict2 = dict(name="Mohamed" , age=40 , city="makaa")

print(mydict2)

val = mydict["name"]

print(val)

# mutable

mydict["name"] = "not zedan"

# mydict.pop("age")
mydict.popitem() # remove last added key
print(mydict)

if "name" in mydict:
    print("name is exist in mydict")

del mydict
