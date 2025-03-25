def solution(babbling):
    answer = 0
    for bab in babbling:
        count = 0
        aya, woo, ye, ma = True, True, True, True
        while bab != "":
            word3 = bab[:3]
            word2 = bab[:2]
            if word3 == "aya" and aya:
                aya = False
                bab = bab[3:]
                count += 1
                continue
            if word3 == "woo" and woo:
                woo = False
                bab = bab[3:]
                count += 1
                continue
            if word2 == "ye" and ye:
                ye = False
                bab = bab[2:]
                count += 1
                continue
            if word2 == "ma" and ma:
                ma = False
                bab = bab[2:]
                count += 1
                continue
            break
        if bab == "":
            answer += 1
    return answer