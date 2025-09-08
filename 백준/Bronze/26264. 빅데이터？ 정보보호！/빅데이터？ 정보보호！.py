n = int(input())
string = input()

s = string.count("security")
b = string.count("bigdata")

if s > b:
    print("security!")
elif s< b:
    print("bigdata?")
else:
    print("bigdata? security!")