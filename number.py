import requests
import json
import os
import time
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
                                  ░   ''')

class PhoneNumberInfo:
    def __init__(self):
        self.htmlweb_api_url = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.cache_file = 'phone_cache.json'
        self._load_cache()

    def _load_cache(self):
        try:
            with open(self.cache_file, 'r') as file:
                self.cache = json.load(file)
        except FileNotFoundError:
            self.cache = {}

    def _save_cache(self):
        with open(self.cache_file, 'w') as file:
            json.dump(self.cache, file)

    def get_number_data(self, user_number):
        if user_number in self.cache:
            return self.cache[user_number]

        response_htmlweb = requests.get(self.htmlweb_api_url + user_number)

        if response_htmlweb.ok:
            data_htmlweb = response_htmlweb.json()

            self.cache[user_number] = data_htmlweb
            self._save_cache()
            return data_htmlweb
        else:
            return {"status_error": True}

    def print_number_info(self):
        user_number = input("Введите номер телефона (например, +79833170773): ").strip()

        if user_number:
            print("Поиск данных...\n")
            data = self.get_number_data(user_number)

            if data.get("status_error"):
                print("Ошибка: Не удалось получить данные. Проверьте номер телефона и попробуйте снова.")
                return

            country = data.get('country', {})
            region = data.get('region', {})
            other = data.get('0', {})

            print(f"Страна: {country.get('name', 'Не найдено')}, {country.get('fullname', 'Не найдено')}")
            print(f"Город: {other.get('name', 'Не найдено')}")
            print(f"Почтовый индекс: {other.get('post', 'Не найдено')}")
            print(f"Код валюты: {country.get('iso', 'Не найдено')}")
            print(f"Телефонные коды: {data.get('capital', {}).get('telcod', 'Не найдено')}")
            print(f"Посмотреть в wiki: {other.get('wiki', 'Не найдено')}")
            print(f"Гос. номер региона авто: {region.get('autocod', 'Не найдено')}")
            print(f"Оператор: {other.get('oper', 'Не найдено')}, {other.get('oper_brand', 'Не найдено')}, {other.get('def', 'Не найдено')}")
            print(f"Местоположение: {country.get('name', 'Не найдено')}, {region.get('name', 'Не найдено')}, {other.get('name', 'Не найдено')} ({region.get('okrug', 'Не найдено')})")

            latitude = other.get('latitude', 'Не найдено')
            longitude = other.get('longitude', 'Не найдено')
            location = data.get('location', 'Не найдено')
            lang = country.get('lang', 'Не найдено').title()
            lang_code = country.get('langcod', 'Не найдено')
            capital = data.get('capital', {}).get('name', 'Не найдено')

            print(f"Открыть на карте (google): https://www.google.com/maps/place/{latitude}+{longitude}")
            print(f"Локация: {location}")
            print(f"Язык общения: {lang}, {lang_code}")
            print(f"Край/Округ/Область: {region.get('name', 'Не найдено')}, {region.get('okrug', 'Не найдено')}")
            print(f"Столица: {capital}")
            print(f"Широта/Долгота: {latitude}, {longitude}")
            print(f"Оценка номера в сети: https://phoneradar.ru/phone/{user_number}")

        else:
            print("Ошибка: Номер телефона не введен.")

if __name__ == "__main__":
    phone_info = PhoneNumberInfo()
    phone_info.print_number_info()
