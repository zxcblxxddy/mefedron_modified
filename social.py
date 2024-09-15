import os
from googlesearch import search
from pystyle import Colors, Colorate

# Функция для очистки консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def search_social_media(query):
    clear_console()
    print(Colorate.Horizontal(Colors.red_to_white, f"Поиск профилей в социальных сетях для: {query}\n"))
    
    search_queries = [
        f"{query} site:facebook.com",
        f"{query} site:instagram.com",
        f"{query} site:twitter.com",
        f"{query} site:linkedin.com"
    ]

    results = []
    for q in search_queries:
        count = 0
        for result in search(q):
            if count >= 5:
                break
            results.append(result)
            count += 1
    
    if results:
        print(Colorate.Horizontal(Colors.red_to_white, "\nНайденные профили:"))
        for result in results:
            print(Colorate.Horizontal(Colors.red_to_white, result))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Информация не найдена."))

def main():
    clear_console()
    query = input(Colorate.Horizontal(Colors.red_to_white, "Введите имя или email для поиска: "))
    search_social_media(query)

if __name__ == "__main__":
    main()