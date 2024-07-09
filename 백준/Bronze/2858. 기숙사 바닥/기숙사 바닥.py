R, B = map(int, input().split())
room = R + B

for i in range(3, 10**6):
    if room % i == 0:
        if ((i + room//i)*2 - 4 == R) and room - ((i + room//i)*2 - 4) == B:
            print(room//i, i)
            break
