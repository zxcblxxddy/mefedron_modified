import os
import csv
import requests
from bs4 import BeautifulSoup
class TerminalColors:
    END = '\033[0m'
    RESULT_COLOR = '\033[38;2;0;255;0m'

def generate_red_to_white_gradient(steps=30):
    colors = [
        (255, 0, 0),    # Красный
        (255, 255, 255) # Белый
    ]

    gradient_colors = []
    n = len(colors)
    for i in range(steps):
        frac = i / steps
        idx1 = int(frac * (n - 1))
        idx2 = min(idx1 + 1, n - 1)
        t = frac * (n - 1) - idx1
        r = int(colors[idx1][0] * (1 - t) + colors[idx2][0] * t)
        g = int(colors[idx1][1] * (1 - t) + colors[idx2][1] * t)
        b = int(colors[idx1][2] * (1 - t) + colors[idx2][2] * t)
        gradient_colors.append(f'\033[38;2;{r};{g};{b}m')

    return gradient_colors

def clear_screen():
    # Проверка операционной системы
    if os.name == 'nt':  # Windows
        os.system('cls')

def apply_gradient(text, colors):
    colored_text = ""
    color_length = len(colors)
    for i, char in enumerate(text):
        if char == '\n':
            colored_text += char
        else:
            colored_text += colors[i % color_length] + char
    return colored_text + TerminalColors.END

def display_logo():
    logo = r"""
      ___           ___           ___           ___           ___                    ___           ___                 
     /__/\         /  /\         /__/\         /__/\         /  /\                  /  /\         /  /\          ___   
    _\_ \:\       /  /::\        \  \:\        \  \:\       /  /::\                /  /:/        /  /::\        /__/|  
   /__/\ \:\     /  /:/\:\        \  \:\        \  \:\     /  /:/\:\              /  /:/        /  /:/\:\      |  |:|  
  _\_ \:\ \:\   /  /:/~/::\   _____\__\:\   _____\__\:\   /  /:/~/::\            /  /:/  ___   /  /:/~/:/      |  |:|  
 /__/\ \:\ \:\ /__/:/ /:/\:\ /__/::::::::\ /__/::::::::\ /__/:/ /:/\:\          /__/:/  /  /\ /__/:/ /:/___  __|__|:|  
 \  \:\ \:\/:/ \  \:\/:/__\/ \  \:\~~\~~\/ \  \:\~~\~~\/ \  \:\/:/__\/          \  \:\ /  /:/ \  \:\/:::::/ /__/::::\  
  \  \:\ \::/   \  \::/       \  \:\  ~~~   \  \:\  ~~~   \  \::/                \  \:\  /:/   \  \::/~~~~     ~\~~\:\ 
   \  \:\/:/     \  \:\        \  \:\        \  \:\        \  \:\                 \  \:\/:/     \  \:\           \  \:\ 
    \  \::/       \  \:\        \  \:\        \  \:\        \  \:\                 \  \::/       \  \:\           \__\/
     \__\/         \__\/         \__\/         \__\/         \__\/                  \__\/         \__\/                 
"""
    gradient_colors = generate_red_to_white_gradient()
    colored_logo = apply_gradient(logo, gradient_colors)
    print(colored_logo)

def display_menu():
    menu = '''                               main | dev @happispython | version 1.0.0

        =======================================================================================================
        ||1. Universal Search || 11. Поиск по DOMEN    || 21. Поиск по PASSWORD   ||  31. Поиск по RFID      ||
        ||2. Поиск по WEBSITE || 12. Поиск по LOGIN    || 22. Поиск по PASSPORT   ||  32. Поиск по OSAGO     ||
        ||3. Поиск по NICK    || 13. Поиск по SNILS    || 23. Поиск по FACEBOOK   ||  33. Поиск по CONTRACT  ||
        ||4. Поиск по INN     || 14. Поиск по TELEGRAM || 24. Поиск по INSTAGRAM  ||  34. Поиск по GIS       ||
        ||5. Поиск по VK      || 15. Поиск по TIKTOK   || 25. Поиск по USER-AGENT ||  35. Поиск по GMP       ||
        ||6. Поиск по OK      || 16. Поиск по HWID     || 26. Поиск по SPOTIFY    ||  36. Поиск по EGRIP     ||
        ||7. Поиск по MAC     || 17. Поиск по DOCUMENT || 27. Поиск по EMAIL      ||  37. Поиск по RDTS      ||
        ||8. Поиск по CARD    || 18. Поиск по SIGNAL   || 28. Поиск по IMEI       ||  38. Поиск по GPS-Cords ||
        ||9. Поиск по DISCORD || 19. Поиск по NUMBER   || 29. Поиск по IMSI       ||  39. Поиск по POLICY    ||
        ||10. Поиск по F.I.O  || 20. Поиск по IP       || 30. Поиск по UDID       ||  40. Поиск по LICENSE   ||
        =======================================================================================================
'''
    gradient_colors = generate_red_to_white_gradient()
    colored_menu = apply_gradient(menu, gradient_colors)
    print(colored_menu)

def search_in_file(filename, keyword):
    results = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword.lower() in line.lower():
                results.append(line.strip())
    return results
def search_in_website(url, keyword):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Ищем все элементы, которые могут содержать ключевое слово
        elements = soup.find_all(text=lambda text: text and keyword.lower() in text.lower())

        # Возвращаем список найденных элементов
        results = [element.strip() for element in elements if element.strip()]
        return results

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
        return []

def search_in_csv(filename, keyword):
    results = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if any(keyword.lower() in cell.lower() for cell in row):
                results.append(row)
    return results

def search_all_files(base_path, keyword):
    results = {}
    files = os.listdir(base_path)

    for filename in files:
        file_path = os.path.join(base_path, filename)
        if filename.endswith(('.txt', '.csv')):
            if filename.endswith('.txt'):
                results[filename] = search_in_file(file_path, keyword)
            elif filename.endswith('.csv'):
                results[filename] = search_in_csv(file_path, keyword)

    return results

def main():
    while True:
        try:
            clear_screen()
            display_logo()
            display_menu()

            choice = input("Введите номер выбора или 'q' для выхода: ")
            if choice.lower() == 'q':
                break
            if choice == "1":
                keyword = input("Введите ключевое слово для поиска: ")
                base_path = 'C:/users/base'
                all_results = search_all_files(base_path, keyword)

                print(TerminalColors.RESULT_COLOR + "Результаты поиска:" + TerminalColors.END)
                for file, results in all_results.items():
                    if results:
                        print(TerminalColors.RESULT_COLOR + f"\nФайл: {file}" + TerminalColors.END)
                        for result in results:
                            print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

            elif choice == "2":
                url = input("Введите URL веб-сайта: ")
                keyword = input("Введите ключевое слово для поиска: ")
                website_results = search_in_website(url, keyword)

                print(TerminalColors.RESULT_COLOR + "Результаты поиска на сайте:" + TerminalColors.END)
                for result in website_results:
                    print(TerminalColors.RESULT_COLOR + result + TerminalColors.END)

            elif choice == "3":
                keyword = input("Введите NICK для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено.")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")

            elif choice == "4":
                keyword = input("Введите INN для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено.")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")
            elif choice == "5":
                keyword = input("Введите VK ID для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено.")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")

            elif choice == "6":
                keyword = input("Введите OK для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено. добавьте бд  OK")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")
            elif choice == "7":
                keyword = input("Введите MAC для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено. добавьте бд MAC")
                    else:
                        print("Некорректный номер файла. добавьте бд MAC")
                except ValueError:
                    print("Некорректный ввод номера файла.")
            elif choice == "8":
                keyword = input("Введите CARD для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено.")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")
            elif choice == "9":
                keyword = input("Введите DISCORD для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено. добавьте бд  OK")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")
            elif choice == "10":
                keyword = input("Введите F.I.O для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено.")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")
            elif choice == "11":
                keyword = input("Введите DOMEN для поиска: ")
                base_path = 'C:/users/base'
                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")
                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")
                try:
                    file_idx = int(file_choice) - 1
                    if 0 <= file_idx < len(files):
                        file_to_search = files[file_idx]
                        file_path = os.path.join(base_path, file_to_search)
                        if file_to_search.endswith('.txt'):
                            results = search_in_file(file_path, keyword)
                        elif file_to_search.endswith('.csv'):
                            results = search_in_csv(file_path, keyword)

                        print(
                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)
                        if results:
                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)
                        else:
                            print("Ничего не найдено.")
                    else:
                        print("Некорректный номер файла.")
                except ValueError:
                    print("Некорректный ввод номера файла.")


            elif choice == "12":

                keyword = input("Введите LOGIN для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "13":

                keyword = input("Введите SNILS для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "14":

                keyword = input("Введите TELEGRAM ID для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "15":

                keyword = input("Введите TIKTOK для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "16":

                keyword = input("Введите HWID для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "17":

                keyword = input("Введите DOCUMENT для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "18":

                keyword = input("Введите SIGNAL для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "19":

                keyword = input("Введите NUMBER для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "20":

                keyword = input("Введите IP для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "21":

                keyword = input("Введите PASSWORD для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "22":

                keyword = input("Введите PASSPORT для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)

                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)

                        else:

                            print("Ничего не найдено.")

                    else:

                        print("Некорректный номер файла.")

                except ValueError:

                    print("Некорректный ввод номера файла.")



            elif choice == "23":

                keyword = input("Введите FACEBOOK id для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "24":

                keyword = input("Введите INST для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "25":

                keyword = input("Введите USER-GRANT для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "26":

                keyword = input("Введите SPOTIFY для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "27":

                keyword = input("Введите EMAIL для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "28":

                keyword = input("Введите IMEI для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "29":

                keyword = input("Введите IMSI для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "30":

                keyword = input("Введите UDID для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)


                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)


                        else:

                            print("Ничего не найдено.")


                    else:

                        print("Некорректный номер файла.")


                except ValueError:

                    print("Некорректный ввод номера файла.")




            elif choice == "31":

                keyword = input("Введите RFID для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "32":

                keyword = input("Введите OSAGO для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "33":

                keyword = input("Введите CONTRACT для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "34":

                keyword = input("Введите GIS для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "35":

                keyword = input("Введите GMP для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "36":

                keyword = input("Введите EGRIP для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "37":

                keyword = input("Введите RDTS для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "38":

                keyword = input("Введите GPF-Cord для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "39":

                keyword = input("Введите POLICY для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")





            elif choice == "40":

                keyword = input("Введите LICENSE для поиска: ")

                base_path = 'C:/users/base'

                files = os.listdir(base_path)

                print("\nВыберите файл для поиска:")

                for idx, filename in enumerate(files, 1):
                    print(f"{idx}. {filename}")

                file_choice = input("\nВведите номер файла: ")

                try:

                    file_idx = int(file_choice) - 1

                    if 0 <= file_idx < len(files):

                        file_to_search = files[file_idx]

                        file_path = os.path.join(base_path, file_to_search)

                        if file_to_search.endswith('.txt'):

                            results = search_in_file(file_path, keyword)



                        elif file_to_search.endswith('.csv'):

                            results = search_in_csv(file_path, keyword)

                        print(

                            TerminalColors.RESULT_COLOR + f"Результаты поиска по NICK '{keyword}' в файле '{file_to_search}':" + TerminalColors.END)

                        if results:

                            for result in results:
                                print(TerminalColors.RESULT_COLOR + str(result) + TerminalColors.END)



                        else:

                            print("Ничего не найдено.")



                    else:

                        print("Некорректный номер файла.")



                except ValueError:

                    print("Некорректный ввод номера файла.")




            else:
                print(f"\nВы выбрали: {choice}")
                # Здесь можно добавить логику для других опций
            input("\nНажмите Enter для продолжения...")

        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break
        except Exception as e:
            print(f"Ошибка: {e}")



if __name__ == "__main__":
    main()
