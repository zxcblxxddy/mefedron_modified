import os
import random

COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}

os.system("cls")
print(f'''{COLOR_CODE["GREEN"]}     
''')                 
print("[$] Сколько СНИЛСОВ сгенерировать? Максимум - 1000:")
count = int(input())
if count > 1000:
                print("Ошибка: Вы ввели число больше 1000.")
else:                                                                                               

 def generate_snils():
    snils = ''
    for _ in range(9):
        snils += str(random.randint(0, 9))
    checksum = int(snils) % 101
    if checksum < 10:
        snils += '0' + str(checksum)
    else:
        snils += str(checksum)
    return snils[:3] + '-' + snils[3:6] + '-' + snils[6:9] + ' ' + snils[9:]


num_snils_to_generate = 1000
snils_set = set()
while len(snils_set) < num_snils_to_generate:
    snils_set.add(generate_snils())

for snils in snils_set:
    print(snils)