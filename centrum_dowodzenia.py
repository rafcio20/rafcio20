import requests
import socket
import psutil
import os
import time

# Pobranie zewnętrznego IP
def get_external_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "Brak połączenia"

# Pobranie lokalnego IP
def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Brak adresu lokalnego"

# Pobranie lokalizacji po IP
def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"{response.get('country', 'Nieznany')}, {response.get('city', 'Nieznane')}"
    except:
        return "Brak danych lokalizacji"

# Sprawdzenie statusu sieci
def is_connected():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

# Czyści terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Centrum dowodzenia
def control_center():
    while True:
        clear()
        print("📡  MINI CENTRUM DOWODZENIA  📡\n")
        
        online = is_connected()
        print(f"🌍 Status połączenia: {'✅ Online' if online else '❌ Offline'}")

        local_ip = get_local_ip()
        print(f"🏠 Lokalny IP: {local_ip}")

        external_ip = get_external_ip()
        print(f"🌐 Zewnętrzny IP: {external_ip}")

        location = get_location(external_ip)
        print(f"📍 Lokalizacja: {location}")

        # Symulacja VPN - jeśli zewnętrzny IP ≠ lokalny IP, zakładamy że działa VPN lub proxy
        if external_ip != local_ip and external_ip != "Brak połączenia":
            print("🛡️  VPN lub proxy: WŁĄCZONE")
        else:
            print("🛡️  VPN lub proxy: WYŁĄCZONE")

        print("\n⏳ Odświeżanie za 15 sekund... (Ctrl + C by exit)")
        time.sleep(15)

if __name__ == '__main__':
    control_center()
