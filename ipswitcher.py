import requests
import random
import time

# Lista przykładowych proxy — wstaw tutaj swoje lub darmowe z neta
proxy_list = [
    'http://51.158.68.133:8811',
    'http://185.199.229.156:7492',
    'http://159.203.61.169:8080'
]

# Funkcja do pobierania IP przez proxy
def get_ip_through_proxy(proxy):
    try:
        response = requests.get('https://httpbin.org/ip', proxies={
            'http': proxy,
            'https': proxy
        }, timeout=5)
        return response.json()['origin']
    except Exception as e:
        return f'❌ Proxy failed: {proxy}'


def start_switcher_interactive():
    while True:
        proxy = random.choice(proxy_list)
        print(f'\n🌐 Using proxy: {proxy}')
        current_ip = get_ip_through_proxy(proxy)
        print(f'🆔 Your IP: {current_ip}')
        
        cont = input("🔁 Chcesz sprawdzić kolejne proxy? (t/n): ").strip().lower()
        if cont != 't':
            print("👋 Zakończono.")
            break

if __name__ == '__main__':
    start_switcher_interactive()
