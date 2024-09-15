import os
import random

COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}

os.system("cls")
print(f'''{COLOR_CODE["GREEN"]}     
''')                                                                                               
print("[$] Сколько карт сгенерировать? Максимум - 1.000.000:")
try:
            count = int(input())
            if count > 1000000:
                print("Ошибка: Вы ввели число больше 1000000.")
            else:
                with open("Базы\data42.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()
                for line in lines:
                    data = line.strip().split('|')

                generated_lines = [random.choice(lines) for _ in range(count)]
                print("Сгенерировано:")
                for line in generated_lines:
                    print(line, end="")
except ValueError:
     print("Ошибка: Введено некорректное число.")
     input("Нажмите Enter, чтобы продолжить...") 
