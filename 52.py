def max_factor(num):
    """Find the maximum prime factor."""
    factor = 2
    while factor * factor <= num:
        while num % factor == 0:
            num /= factor
        factor += 1
    if (num > 1):
        return num
    return factor
sum1 = 0
for i in range(1,10000):
    sum1 = sum1 + max_factor(i*i+1) 
    
print (sum1)
