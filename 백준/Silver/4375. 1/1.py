import sys
sys.set_int_max_str_digits(10**7)

while True:
    try:
        n = int(input())
    except:
        break
    while True:    
        one = '1' * (len(str(n)))
        while int(one) % n != 0:
            one += '1'
        print(len(one))
        break