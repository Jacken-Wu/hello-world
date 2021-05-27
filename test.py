a = float(input())
if a < 20:
    fx = 6 * a * a + 1
elif a <= 40:
    fx = (3 * a + 6) ** 0.5
else:
    fx = 100 / (a + 1)
print('%.2f' % fx)
