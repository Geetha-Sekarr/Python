#list
a=[10,12,8,4,7]
a.append(25)
a.append("true")
print(a)

#duplicate value
a.append(10)
print(a)
a.insert(1,20)
print(a)
a.insert(3,"geetha")
print(a)

#Modify value
a[0]="prema"
print(a)

#remove value
a.pop(4)
print(a)
a.pop()
print(a)

#extend value
b=[1,2,3,4,5]
a.extend(b)
print(a)


#Tuples Example
c=(10,11,12,15,22)
h=list(c)
print(h)

#Sets Example
place={90,23,46,87,66}
# place.remove(90)
# place.pop()#pop takes no argument and unordered set so it will print always unordered values
print(place)
place.add(1)
print(place)
place.discard(23)

d={
    "name":"geetha","age":23, "students":["prema","madurai"]
}
print(d)
print(d.keys())
print(d.values())
d["age"]=22
print(d)
d["color"]="red"
d.update({"location":"chennai"})
d.pop("age")
#d.del["age"]
#d.clear()
print(d)

d={"name":"geetha","age":23,"color":"red","fruits":"apple"}
d.update({"color":"orange"})
print(d)


a=dict()
a={x: ord(x) for x in "hello"}
v={x for x in a.values()}
print(v)