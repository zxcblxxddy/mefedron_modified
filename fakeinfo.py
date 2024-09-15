import random
import os
from faker import Faker

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

def generate_fake_identity():
    fake = Faker('ru_RU')
    identity = f"""
    full name >
            Имя : {fake.first_name()}
            Фамилия : {fake.last_name()}
            Date of Brith : {fake.date_of_birth()}
            Job : {fake.job()}
    Address > 
            Address : {fake.address()}
            IPv4-Adress : {fake.ipv4()}
            Private IPv4 : {fake.ipv4_private()}
            Mac-Adress : {fake.mac_address()}
            IPv6-Adress : {fake.ipv6()} 
    Email >    
            Email > {fake.email()}
            Password > {fake.password()}
    Phone Number > 
            Phone Number > {fake.phone_number()}
    Credit Card >
            Credit Card Number > {fake.credit_card_number()}
    Passport > 
            Passport Number : {fake.passport_number()}
            Passport dob : {fake.passport_dob()}
            Passport Gender : {fake.passport_gender()}
            Passport Data : {fake.passport_dates()}
"""
    return identity

print(generate_fake_identity())