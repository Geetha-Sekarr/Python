x=lambda a,b:a*b
print(x(3,5))

#using anonymous function
def myfunct(n):
    return lambda a:a*n
mydoubler=myfunct(2)
mytripler=myfunct(3)
print(mydoubler(11))
print(mytripler(12))

#with map function
numbers=[1,2,3,4,5]
s=list(map(lambda x:x**2, numbers))
print(s)

#filter function
numbers=[1,2,3,4,5,6,7]
sfilter=list(filter(lambda a:a%2==0,numbers))
print(sfilter)

#characters 
words=["apple","mango","orange","potato","banana"]
long_words=list(filter(lambda word: len(word) >3, words))
print(long_words)

words = ["apple", "cat", "banana", "dog", "elephant"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)