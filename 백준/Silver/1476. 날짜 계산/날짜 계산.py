e, s, m = map(int, input().split())

# e = 15, s = 28, m = 19

e_e = 0
e_s = 0
e_m = 0

year = 0
while e != e_e or s != e_s or m != e_m:
    e_e += 1
    e_s += 1
    e_m += 1
    e_e = e_e % 15
    e_s = e_s % 28
    e_m = e_m % 19
    e = e%15
    s = s%28
    m = m%19
    year += 1

print(year)