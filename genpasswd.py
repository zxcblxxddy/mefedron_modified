import os
import random
import string
COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}

os.system("cls")
print(f'''{COLOR_CODE["GREEN"]}     
                                                                                                                                                                                                                                                                                                                                        
''')                                                                                                 
print("[$] Сколько паролей сгенерировать? Максимум - 100000:")
count = int(input())
if count > 100000:
                print("Ошибка: Вы ввели число больше 100000.")
else:

    def generate_password(length):
     characters = string.ascii_letters + string.digits + string.punctuation
     return ''.join(random.choice(characters) for _ in range(length))

for _ in range(100000):
    print(generate_password(12))