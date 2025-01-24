g=[3,5,78,9]
for num in g:
    print(num)
    
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i,a[i])
    continue

#while loop
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')