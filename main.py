import art
import random

print("Taş, Kağıt, Makas Oyununa Hoş geldiniz.")
which_choice = input("Ne seçmek İstersin? Taş?, Kağıt?, Makas?").lower()
secimler = (art.rock, art.paper, art.scissors)

if which_choice == "taş":
    computer_choice = random.choice(secimler)
    print(f"Senin Seçimin\n {art.rock}")
    if computer_choice == art.rock:
        print(f"Bilgisayar Seçimi\n {art.rock}\n Berabere")
    elif computer_choice == art.paper:
        print(f"Bilgisayar Seçimi\n {art.paper}\n Bilgisayar Kazandı")
    elif computer_choice == art.scissors:
        print(f"Bilgisayar Seçimi\n {art.scissors}\n Sen Kazandın")
elif which_choice == "kağıt":
    computer_choice = random.choice(secimler)
    print(f"Senin Seçimin\n {art.paper}")
    if computer_choice == art.rock:
        print(f"Bilgisayar Seçimi\n {art.rock}\n Sen Kazandın")
    elif computer_choice == art.paper:
        print(f"Bilgisayar Seçimi\n {art.paper}\n Berabere")
    elif computer_choice == art.scissors:
        print(f"Bilgisayar Seçimi\n {art.scissors}\n Bilgisayar Kazandı")
elif which_choice == "makas":
    computer_choice = random.choice(secimler)
    print(f"Senin Seçimin\n {art.scissors}")
    if computer_choice == art.rock:
        print(f"Bilgisayar Seçimi\n {art.rock}\n Bilgisayar Kazandı")
    elif computer_choice == art.paper:
        print(f"Bilgisayar Seçimi\n {art.paper}\n Sen Kazandın")
    elif computer_choice == art.scissors:
        print(f"Bilgisayar Seçimi\n {art.scissors}\n Berabere")
else:
    print("Yanlış bir seçim yaptınız lütfen tekrar deneyiniz.")