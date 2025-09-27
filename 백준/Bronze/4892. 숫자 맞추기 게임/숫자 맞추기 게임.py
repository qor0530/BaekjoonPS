tries = 1
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 1:
        print(f"{tries}. odd {(n//2)}")
    else:
        print(f"{tries}. even {(n//2)}")
    tries += 1