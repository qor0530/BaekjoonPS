string = list(map(str, input().split()))
while string != ["*"]:
    key = string[0][0].upper()
    for i in string:
        if i[0].upper() != key:
            print("N")
            break
    else:
        print("Y")
    string = list(map(str, input().split()))
