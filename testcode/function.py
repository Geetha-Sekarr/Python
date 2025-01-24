def my_function(first_name,lastname):
  print(first_name,lastname)

my_function("geetha","sekar")

def name(email):
  print(email+"@gmail.com")
name("geetha242002")
name("prema2490")

#default arguments
def my_name(name="prema"):
  print(name)
my_name()

#keyword arguments
def describe_person(name, age, city):
    print(f"Nmae:{name},Age:{age},City:{city}")
describe_person(name="Alice", age=30, city="chennai")

def non_argument(fruits,color):
   print(f"Fruit Name:{fruits},Color:{color}")
non_argument("apple",color="yellow")


def introduce(name, age, city="Madurai"):
    print(f"Name: {name}, Age: {age}, City: {city}")

introduce("Alice", 30)
introduce("Bob", 25, city="New York")
introduce("string",23,city="Chennai")

#*argument
def non_argument(*place):
   print("This is non-argument" +place[1])
non_argument("chennai","Madurai","Arupukottai")

#keyword arguments
def key_word(**kids):
   print("Dress collections" +kids["size"])
key_word(product_name="shirts",size="xl")


# without arbitary arguments
a=[1,2,3,4,5]
def arbitary_name(numbers):
    total=0
    for i in numbers:
      total=total+i
    return total
print(arbitary_name(a))

#with arbitray arguments
def arbitary_name(*number):
   total=0
   for i in number:
      total=total+i
   return total
print(arbitary_name(1,2,3,4,5,6,7)) 

#return
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#unpacking arguments
def fun(a, b, c, d):
    print(a, b, c, d)
my_list = [1, 2, 3, 4]
fun(*my_list) 