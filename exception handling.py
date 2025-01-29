try:
    a=int(input())
    b=int(input())
    print(a+b)
except ValueError as e:
    print("value error")
except TypeError as e:
    print("type error")
except Exception as e:
    print("something",e)
finally:
    print("done")