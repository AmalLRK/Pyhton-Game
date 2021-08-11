import random

attempts = 0
digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digit_code_v0 = 0
num = 0

def checkPin(guessed_pin) :
    global attempts
    tab_res = []
    initialAttemp()
    digit_code = list(digit_code_v0)
    mon_tab = []
    attempts += 1
    print("attempts : ", attempts)
    try:
        mon_tab = []
        n = int(guessed_pin)
        for element in guessed_pin:
            mon_tab.append(element)
        if len(mon_tab) != 4:
            tab_res.extend([100, attempts])
            return tab_res

    except:
        tab_res.extend([100, attempts])
        return tab_res

    if (mon_tab == digit_code):
        tab_res.extend([200, attempts])
        return tab_res

    else:
        tabl1i = ["1wi", "1xi", "1yi", "1zi"]
        tabl2i = ["2wi", "2xi", "2yi", "2zi"]
        tabl1j = ["1wj", "1xj", "1yj", "1zj"]
        tabl2j = ["2wj", "2xj", "2yj", "2zj"]
        count = 0
        count2 = 0
        for i in range(0, 4):
            if (mon_tab[i] == digit_code[i]):
                mon_tab[i] = tabl1i[i]
                digit_code[i] = tabl2i[i]
                count += 1
            else:
                continue
        for i in range(0, 4):
            for j in range(0, 4):
                if (mon_tab[i] == digit_code[j]):
                    if i == j:
                        continue
                    else:
                        mon_tab[i] = tabl1j[i]
                        digit_code[j] = tabl2j[j]
                        count2 += 1
                else:
                    continue
        if ((count != 0)  or (count2 != 0) ):
            tab_res.extend([count, count2, attempts])
            return tab_res
            print(digit_code)

        else :
            tab_res.extend([300, attempts])
            return tab_res


def initialAttemp() :
    global attempts, digit_code_v0, num
    if (attempts == 10 or attempts == 0) :
        attempts = 0
        digit_code_v0 = random.sample(digit, 4)
        num = (''.join(map(str, digit_code_v0)))
        print(digit_code_v0)

