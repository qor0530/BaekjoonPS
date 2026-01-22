a1, b1, a2, b2 = map(int, input().split())
gg=(a1+b1)/2+(a2+b2)/2
a1, b1, a2, b2 = map(int, input().split())
su=(a1+b1)/2+(a2+b2)/2

if gg == su:
    print("Tie")
elif gg > su:
    print("Gunnar")
else:
    print("Emma")