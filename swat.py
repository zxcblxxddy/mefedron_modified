import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

def replace_chars(text, use_fence):
    replacements = {
        'А': 'А', 'а': 'а', 'Б': 'Б', 'б': 'б', 'В': 'B', 'в': 'в', 'Г': 'Г', 'г': 'г', 
        'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'Ё', 'ё': 'ё', 'Ж': 'Ж', 'ж': 'Ж', 
        'З': '3', 'з': '3', 'И': 'U', 'и': 'u', 'й': 'й', 'К': 'K', 'к': 'k', 'Л': 'JI', "л": "JI",
        'М': 'M', 'м': 'м', 'Н': 'Н', 'н': 'н', 'о': '0', 'п': 'n', 'р': 'p', 'с': 'c', "С": "S",
        'т': 'T', 'у': 'y', 'ф': 'ф', 'х': 'x', 'ч': '4', "Ч": "4",'ш': 'III', "Ш": "III", 'щ': 'щ', 'ъ': 'ъ', 
        'ы': 'bI', "Ы": "bI", 'ю': 'ю', 'я': 'я'
    }
    result = ''
    for char in text:
        if use_fence:
            result += replacements.get(char.upper(), char)
        else:
            result += replacements.get(char.upper(), char.upper())
    return result
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

def print_developer_info():
    print("Разработчик: @ikeapanic\n")

print_developer_info()

print("1. ВыВоД вИдЕ зАбОрА.\n2. ВСЕ ЗАГЛАВНЫЕ.\n")
option = input("Выберите опцию:")
if option not in ['1', '2']:
    print("Ошибка: Неправильная опция.")
    exit()

clear_console()

if option == '1':
    user_input = input("Введите текст: ")
    replaced_text = replace_chars(user_input, True)
    clear_console()
    print("Результат замены:\n")
    print(replaced_text)
else:
    user_input = input("Введите текст: ")
    replaced_text = replace_chars(user_input, False)
    clear_console()
    print("Результат замены:\n")
    print(replaced_text)
