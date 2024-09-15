#да скопипастила ичо
import os
import sys
import subprocess
import time

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"
BLACK_BG = "\033[40m"

required_modules = [
    "pystyle",
    "randmac",
    "username",
    "pyfiglet",
    "urllib3",
    "phonenumbers",
    "colored",
    "banner",
    "colorama",
    "python-whois",
    "requests",
    "bs4",
    "faker",
    "datetime",
    "defusedxml"
]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def check_and_install_modules():
    print(
        GREEN_TEXT + "Вас приветствует мастер установки mefedron'a \nСейчас мы проведем установку всех зависимостей для правильной работы программы\nУстановка не займет более 3-х минут.\n3\n2\n1\n" + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module} уже установлен." + RESET)
        except ImportError:
            print(f"Установка {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f"Установлен модуль {module}" + RESET)

def launck():
    subprocess.check_call([sys.executable, 'main.py'])

check_and_install_modules()
launck()