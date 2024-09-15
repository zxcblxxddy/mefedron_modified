from pystyle import Colors, Colorate, Center, Box
import os
import datetime

# Функция для очистки консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция для отображения баннера
def display_banner():
    banner = """
  
 ███▄ ▄███▓▓█████   █████▒▓█████ ▓█████▄  ██▀███   ▒█████   ███▄    █ 
▓██▒▀█▀ ██▒▓█   ▀ ▓██   ▒ ▓█   ▀ ▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ 
▓██    ▓██░▒███   ▒████ ░ ▒███   ░██   █▌▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒
▒██    ▒██ ▒▓█  ▄ ░▓█▒  ░ ▒▓█  ▄ ░▓█▄   ▌▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒
▒██▒   ░██▒░▒████▒░▒█░    ░▒████▒░▒████▓ ░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░
░ ▒░   ░  ░░░ ▒░ ░ ▒ ░    ░░ ▒░ ░ ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░  ░      ░ ░ ░  ░ ░       ░ ░  ░ ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░      ░      ░    ░ ░       ░    ░ ░  ░   ░░   ░ ░ ░ ░ ▒     ░   ░ ░ 
       ░      ░  ░           ░  ░   ░       ░         ░ ░           ░ 
                                  ░                                   

    """
    info_box = """
    OWNER: ikeapanic
    ────────────────────
    Version: 1.0 Beta
    ────────────────────
    Price: free
    """
    combined_banner = f"{banner}{' ' * 5}{info_box}"
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(combined_banner)))

# Функция для создания шаблона докса
def create_dox_template():
    clear_console()
    display_banner()
    
    print(Colorate.Horizontal(Colors.green_to_white, Box.DoubleCube("Создание шаблона докса\n")))

    # Ввод данных
    name = input(Colorate.Horizontal(Colors.green_to_white, "Введите имя: "))
    age = input(Colorate.Horizontal(Colors.green_to_white, "Введите возраст: "))
    dob = input(Colorate.Horizontal(Colors.green_to_white, "Введите дату рождения: "))
    address = input(Colorate.Horizontal(Colors.green_to_white, "Введите адрес: "))
    phone = input(Colorate.Horizontal(Colors.green_to_white, "Введите номер телефона: "))
    email = input(Colorate.Horizontal(Colors.green_to_white, "Введите электронную почту: "))
    card_number = input(Colorate.Horizontal(Colors.green_to_white, "Введите номер карты: "))
    social_media = input(Colorate.Horizontal(Colors.green_to_white, "Введите ссылки на социальные сети: "))
    additional_info = input(Colorate.Horizontal(Colors.green_to_white, "Введите дополнительную информацию: "))

    # Создание шаблона
    template = f"""
    ------------------------------
    DOX Template
    ------------------------------
    Name: {name}
    Age: {age}
    Date of Birth: {dob}
    Address: {address}
    Phone: {phone}
    Email: {email}
    Card Number: {card_number}
    Social Media: {social_media}
    Additional Info: {additional_info}
    ------------------------------
    """
    
    # Сохранение в файл
    file_count = len([f for f in os.listdir('.') if f.startswith('dox_template') and f.endswith('.txt')])
    filename = f'dox_template{file_count + 1}.txt'
    
    with open(filename, 'w') as file:
        file.write(template)
    
    print(Colorate.Horizontal(Colors.green_to_white, template))
    print(Colorate.Horizontal(Colors.green_to_white, f"\nШаблон сохранён в файл {filename}"))

    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

if __name__ == "__main__":
    create_dox_template()
