import math
# всьо тут максимальное значения
y = 1000
rpr = 0.9
mpr = 0.75
apr1 = 0.5
apr2 = 0.25
apr3 = 0.1

y = math.ceil(((y * (1 - rpr)) * (1 - mpr)) * (1 - (apr1 + apr2 + apr3)))
print(y)
input()

