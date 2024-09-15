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
print("[$] Сколько почт сгенерировать? Максимум - 1000:")
count = int(input())
if count > 1000:
                print("Ошибка: Вы ввели число больше 1000.")
else:
    
    def generate_email():
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(domains)
        return f'{username}@{domain}'

for _ in range(1000):
    print(generate_email())