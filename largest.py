a = int(input("enter a number:->"))
def lpf(a):
    b = 2
    while (a > b):
        if (a % b == 0):
            a = a / b;
            b = 2;
        else:
            b += 1;
    print("Largest Prime Factor: %d" % (b))
