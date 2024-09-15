import random
import os

COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}
os.system("cls")
print(f'''{COLOR_CODE["GREEN"]} 

 ███▄ ▄███▓▓█████   █████▒▓█████ ▓█████▄  ██▀███   ▒█████   ███▄    █ 
▓██▒▀█▀ ██▒▓█   ▀ ▓██   ▒ ▓█   ▀ ▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ 
▓██    ▓██░▒███   ▒████ ░ ▒███   ░██   █▌▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒
▒██    ▒██ ▒▓█  ▄ ░▓█▒  ░ ▒▓█  ▄ ░▓█▄   ▌▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒
▒██▒   ░██▒░▒████▒░▒█░    ░▒████▒░▒████▓ ░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░
░ ▒░   ░  ░░░ ▒░ ░ ▒ ░    ░░ ▒░ ░ ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░  ░      ░ ░ ░  ░ ░       ░ ░  ░ ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░      ░      ░    ░ ░       ░    ░ ░  ░   ░░   ░ ░ ░ ░ ▒     ░   ░ ░ 
       ░      ░  ░           ░  ░   ░       ░         ░ ░           ░ 
                                  ░          ''')                                                                                               
print("[$] Сколько номеров сгенерировать? Максимум - 1000:")
count = int(input())
if count > 1000:
                print("Ошибка: Вы ввели число больше 1000.")
else:
 def generate_phone_number():
    phone_number = '+7'
    for _ in range(9):
     phone_number += str(random.randint(0, 9))
    return phone_number


num_phone_numbers_to_generate = 1000
phone_number_set = set()
while len(phone_number_set) < num_phone_numbers_to_generate:
        phone_number_set.add(generate_phone_number())

for phone_number in phone_number_set:
    print(phone_number)
