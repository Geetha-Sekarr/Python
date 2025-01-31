import re 
text="hello world"
a=re.search("^hello",text)
print(a)
#if a is not None:
    #print("match found")
#else:
    #print("match is not found")

#ends with
a=re.search("world $",text)
print(a)

#any character
a=re.findall("hel..",text)
print(a)

#0 or more character
a=re.findall("he.*o",text)
print(a)

# 1 or more character
a=re.findall("he.+o",text)
print(a)



