Csum = 0
GPA = 0
T = int(input())
for i in range(T):
    N = int(input())
    Csum = 0
    GPA = 0
    for j in range(N):
        C, G = map(float, input().split())
        Csum += C
        GPA += G * C
    Csum = int(Csum)
    GPA /= Csum
    GPA = round(GPA, 1)
    print(Csum, GPA)
