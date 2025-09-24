num = 0
for i in range(3):
    a = input()
    if "FizzBuzz" in a:
        pass
    elif "Buzz"   in a:
        pass
    elif "Fizz"   in a:
        pass
    else:
        num = int(a)
    num += 1
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
