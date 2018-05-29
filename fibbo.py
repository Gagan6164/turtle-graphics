def fibbo(n):
    a = 0
    b = 1
    for i in range(n):
        a = b
        b = b + a
        print(a, '/n')
    return b
num = int(input('enter the number value-->')
print(fibbo(num))
