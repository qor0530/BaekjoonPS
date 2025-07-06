n = int(input())

back, front = 1, 1
hap = 0
count = 1

while back != n:
    if hap < n:
        hap += front
        front += 1
    elif hap > n:
        hap -= back
        back += 1
    else:
        count += 1
        hap -= back
        back += 1

print(count)