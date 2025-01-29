#single inheritance and multiple inheritance
class dad():
    def phone(self):
        print("dad phone")
class son(dad):
    def laptop(self):
        print("son laptop")
ram=son()
ram.laptop()
ram.phone()

#multilevel inheritance
class grandpa():
    def money(self):
        print("grandpa money")
class dad(grandpa):
    def phone(self):
        print("Dad phone")
class son(dad):
    def laptop(self):
        print("son2 laptop")
sekar=son()
sekar.money()


#Hierarchical inheritance
class dad():
    def money(self):
        print("dad money")
class son1(dad):
    def watch(self):
        print("watch")
class son2(dad):
    def phone(self):
        print("phone")
class son3(dad):
    def bike(self):
        print("bike")
ram=son2()
ram.money()

#Hybrid inheritance
class dad():
    def money(self):
        print("dad money")
class son1(dad):
    def watch(self):
        print("watch")
class son2(dad):
    def phone(self):
        print("phone")
class son3(son2,dad):
    def bike(self):
        print("bike")
ram=son2()
ram.money()
ram.phone()
ram=son3()
ram.bike()