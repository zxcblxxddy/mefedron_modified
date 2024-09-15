import os
import random

COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}

os.system("cls")
print(f'''{COLOR_CODE["GREEN"]}     
''')                                                                                               
                                                    
print("[$] Сколько ИНН сгенерировать? Максимум - 1000:")
count = int(input())
if count > 1000:
                print("Ошибка: Вы ввели число больше 1000.")
else:
    
    def generate_inn():
        region_code = random.randint(10, 99)  # Двузначный код региона
        individual_number = random.randint(100000, 999999)
        control_number = random.randint(0, 9)

        inn_without_control = f'{region_code:02d}{individual_number:06d}'

        weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
        control_sum = sum(int(digit) * weight for digit, weight in zip(inn_without_control, weights)) % 11 % 10

        return f'{inn_without_control}{control_sum}'

    num_inn_to_generate = 1000
    inn_set = set()
    while len(inn_set) < num_inn_to_generate:
            inn_set.add(generate_inn())

    for inn in inn_set:
            print(inn)