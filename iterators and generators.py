
class Test():
    def __iter__(self):
        self.num = 0
        return self
    def __next__(self):
        if self.num == 10:
            raise StopIteration
        self.num +=1
        return self.num
for i in Test():
    print(i)