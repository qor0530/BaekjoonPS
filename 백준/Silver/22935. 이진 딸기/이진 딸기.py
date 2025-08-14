딸기 = [1, 2, 3, 4, 5, 6, 7, 8,9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5,4 ,3 ,2]
T = int(input())

for i in range(T):
    n = int(input())
    reverse = False
    k = 딸기[n % 28 - 1]
    
    binary = bin(k)[2:]
    while(len(binary) < 4):
        binary = '0' + binary
    binary = binary.replace("1", "딸기")
    binary = binary.replace('0', 'V')
    print(binary)

