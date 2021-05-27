def su(n):
    for i in range(2, n):
        print(i)
        if n % i == 0:
            return False
    return True

a = b = 7
print(su(a))