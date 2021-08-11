import random
digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
attempts = 0
digit_code_v0 = random.sample(digit, 4)
num = (''.join(map(str, digit_code_v0)))
print(digit_code_v0)
attempts = 0

while attempts <10:
        digit_code = list(digit_code_v0)
        mon_tab = []
        attempts += 1
        print("attempts : ", attempts)
        while True:
                try:
                    mon_tab = []
                    guessed_pin = input("Devinez le PIN à 4 chiffres : ")
                    n = int(guessed_pin)
                    for element in guessed_pin:
                        mon_tab.append(element)
                    if len(mon_tab) == 4:
                        break
                    else:
                        print("Ce n'est pas un PIN à 4 chiffres !")
                except:
                    print("Ce n'est pas un PIN à 4 chiffres !")

        if (mon_tab == digit_code):
            print("Génial! Vous avez deviné le nombre ! Vous pouvez commencer le jeux")
            break

        else:
            tabl1i = ["1wi","1xi","1yi","1zi"]
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
               for j in range(0,4):
                   if (mon_tab[i] == digit_code[j]):
                       if i == j:
                           continue
                       else:
                           mon_tab[i] = tabl1j[i]
                           digit_code[j] = tabl2j[j]
                           count2 += 1
                           #print(mon_tab)
                           #print(digit_code)

                   else:
                        continue
            #count2 = count2 - (count*2)
            if ((count < 4) and (count != 0)) or ((count2 <= 4) and (count2 >= 0)):
                print("Pas tout à fait le nombre. Mais tu as eu ", count, " chiffre(s) correct(s)!")
                print("Pas tout à fait le nombre. Mais tu as eu ", count2, " existe mais dans une autre position !")
                print(digit_code)

            elif (count == 0):
                print("Aucun des nombres de votre saisie ne correspond")



