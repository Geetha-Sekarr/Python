#length of the list
a=["Mango","orange","apple"]
print(len(a))

#type of the list
print(type(a))

b=["geetha",20,"sekar",90]
print(b)

#constructor
vv=list(("mango","orange"))
print(vv)

#divide some element
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist[2:3]=["geetha","sekar"]
print(thislist)

#insert
thislist.insert( 2,"prema")

#append
thislist.append("hhh")
print(thislist)

#extend
trop=["icecream","cream","ice"]
thislist.extend(trop)
print(thislist)

#insert
trop.insert(1,"likes")
print(trop)

#remove
trop.remove("cream")
print(trop)

#pop
thislist.pop(1)
print(thislist)

#clear and delete
#thislist.clear()
#thislist.del[0]
thislist.count()
print(thislist)

thislist.append("orange")
print(thislist)

thislist.count("orange")
print(thislist)