

from Config.Util import *
from Config.Config import *
try:
    from json import *
    import requests
    import socket
    if sys.platform.startswith("win"):
        "WINDOWS"
        import win32api
    else:
        pass
except Exception as e:
   ErrorModule(e)
   
Title("Get Your Ip")

try:
    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Your Ip is not sent to anyone.")
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Search your Ip..")
    try:
        hostname_pc = socket.gethostname()
    except:
        hostname_pc = "None"

    try:
        username_pc = os.getlogin()
    except:
        username_pc = "None"

    try:
        if sys.platform.startswith("win"):
            "WINDOWS"
            displayname_pc = win32api.GetUserNameEx(win32api.NameDisplay)
        else:
            displayname_pc = "None"
    except:
        displayname_pc = "None"

    try:
        response = requests.get(f'https://{website}/api/ip/myip')
        ip_address_public = response.json()['ip']
    except:
        ip_address_public = "None"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))  

        ip_address_local = s.getsockname()[0]
        s.close()
    except:
        ip_address_local = "None"

    try:
        ip_address_ipv6 = []
        all_interfaces = socket.getaddrinfo(socket.gethostname(), None)
        for interface in all_interfaces:
            if interface[0] == socket.AF_INET6:
                ip_address_ipv6.append(interface[4][0])
        ip_address_ipv6 = ' / '.join(ip_address_ipv6)
    except:
            ip_address_ipv6 = "None"

    print(f"""
    {INFO_ADD} Pc Hostname      : {white}{hostname_pc}{red}
    {INFO_ADD} Pc Username      : {white}{username_pc}{red}
    {INFO_ADD} Pc DisplayName   : {white}{displayname_pc}{red}
    {INFO_ADD} Ip Public [ipv4] : {white}{ip_address_public}{red}
    {INFO_ADD} Ip Local  [ipv4] : {white}{ip_address_local}{red}
    {INFO_ADD} Ipv6             : {white}{ip_address_ipv6}{red}
    """)


except Exception as e:
    Error(e)