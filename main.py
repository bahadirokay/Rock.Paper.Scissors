import art
import random
language = input("Please choice language.\nWrite 'en' for english\nLütfen Türkçe için 'tr' yazınız\n")
def turkish():
        print("Taş, Kağıt ve Makas oyununa hoş geldiniz.")
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

def english():
        print("Welcome to Rock, Paper and Scissors Game")
        which_choice = input("What do you choose? Rock?, Paper? or Scissors?").lower()
        secimler = (art.rock, art.paper, art.scissors)
        if which_choice == "rock":
            computer_choice = random.choice(secimler)
            print(f"Your choose\n {art.rock}")
            if computer_choice == art.rock:
                print(f"Computer's choose\n {art.rock}\n Draw")
            elif computer_choice == art.paper:
                print(f"Computer's choose\n {art.paper}\n Computer Win")
            elif computer_choice == art.scissors:
                print(f"Computer's choose\n {art.scissors}\n You Win")
        elif which_choice == "paper":
            computer_choice = random.choice(secimler)
            print(f"Your choose\n {art.paper}")
            if computer_choice == art.rock:
                print(f"Computer's choose\n {art.rock}\n You Win")
            elif computer_choice == art.paper:
                print(f"Computer's choose\n {art.paper}\n Draw")
            elif computer_choice == art.scissors:
                print(f"Computer's choose\n {art.scissors}\n Computer Win")
        elif which_choice == "scissors":
            computer_choice = random.choice(secimler)
            print(f"Your choose\n {art.scissors}")
            if computer_choice == art.rock:
                print(f"Computer's choose\n {art.rock}\n Computer Win")
            elif computer_choice == art.paper:
                print(f"Computer's choose\n {art.paper}\n You Win")
            elif computer_choice == art.scissors:
                print(f"Computer's choose\n {art.scissors}\n Draw")
        else:
            print("You made the wrong choice. Please try again.")

if language == 'tr':
    turkish()
elif language == "'tr'":
    turkish()
elif language == 'en':
    english()
elif language == "'en'":
    english()
else:
    print("You made the wrong choice. Please try again.\nYanlış bir seçim yaptınız lütfen tekrar deneyiniz.")