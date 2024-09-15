import os
import random

COLOR_CODE = {
    "GREEN": "\033[0;32m",
    "RESET": "\033[0m",
}

os.system("cls")
print(f'''{COLOR_CODE["GREEN"]}     
''')                    

def generate_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

ip_addresses = [generate_ip() for _ in range(1000)]

for ip in ip_addresses:
    print(ip)