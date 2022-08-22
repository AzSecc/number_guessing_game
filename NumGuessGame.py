import random

numbers = [12, 44, 124, 555, 679, 233, 322, 432, 1324, 1845, 2943]
pr_num = random.choice(numbers)
dif = input("Çətinlik dərəcəsini seç, 'asan' və ya 'çətin' yaz > ")
guess_count_hard = 5
guess_count_easy = 10
guessed_num = 0

while guess_count_hard > 0 and pr_num != guessed_num:
    if dif == 'çətin':
        print(f"Sizin ədədi təxmin etməkçün {guess_count_hard} cəhdiniz var.")
        guessed_num = int(input("Təxmininizi yazın > "))
        if pr_num != guessed_num:
            guess_count_hard = guess_count_hard - 1
            if guess_count_hard == 0:
                print("Şansınız bitdi, uduzdunuz.")
                break
            elif pr_num > guessed_num:
                print("Verilmiş ədəddən kiçikdir.")
            else:
                print("Verilmiş ədəddən böyükdür.")
                print("Yenidən təxmin edin.")
        else:
            print(f"Tapdınız ! Cavab {pr_num} idi.")
    elif dif == 'asan':
        print(f"Sizin ədədi təxmin etməkçün {guess_count_easy} cəhdiniz var.")
        guessed_num = int(input("Təxmininizi yazın > "))
        if pr_num != guessed_num:
            guess_count_easy = guess_count_easy - 1
            if guess_count_easy == 0:
                print("Şansınız bitdi, uduzdunuz.")
                break
            elif pr_num > guessed_num:
                print("Verilmiş ədəddən kiçikdir.")
            else:
                print("Verilmiş ədəddən böyükdür.")
                print("Yenidən təxmin edin.")
        else:
            print(f"Tapdınız ! Cavab {pr_num} idi.")
    else:
        print("Nəysə səhv getdi, yenidən cəhd edin.")
        break
