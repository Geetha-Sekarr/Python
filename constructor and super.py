class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are pretty")
class b():
    def __init__(self):
        super().__init__()
        print("B")
    def display (self):
        print("good girl")
class c(b,a):
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("class c")
fob1=c()
