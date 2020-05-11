import math

input_str = input().split(' ')
a = int(input_str[0])
b = int(input_str[1])
gcd = math.gcd(a, b)
lcd = (math.fabs(a) * math.fabs(b)) // gcd
print(gcd, int(lcd))
