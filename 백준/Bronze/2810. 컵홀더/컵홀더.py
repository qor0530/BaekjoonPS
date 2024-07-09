N = int(input())
sits = input()
sits = sits.split('LL')
count = 0
for i in range(len(sits)):
    sits[i] = sits[i].split('S')
    count += len(sits[i])
if count > N:
    print(N)
else:
    print(count)
