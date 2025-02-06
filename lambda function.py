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



# Lambda that ignores the first argument and returns the second argument
my_lambda = lambda _, y: y

print(my_lambda(10, 20)) 


# List of tuples (name, age)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
names = list(map(lambda _: _[0], people))
print(names) 
