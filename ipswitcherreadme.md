# 🌐 Proxy IP Switcher (Python)

Prosty skrypt w Pythonie do testowania połączeń przez różne serwery proxy oraz rotacji adresów IP. Idealny jako narzędzie edukacyjne do nauki działania proxy, maskowania IP i podstaw bezpieczeństwa sieciowego. Ostatnimi czasy naszlo mnie na sprawdzanie IP i testowanie polaczen oraz na czym polega szyfrowanie adresow IP i jak go maskowac albo ukrywac w sieci.

## 🔧 Funkcje

- Łączy się z zewnętrznym API (`httpbin.org`) przez różne proxy (HTTP/S).
- Wyświetla aktualny publiczny adres IP widoczny przez zewnętrzne serwisy.
- Losowo wybiera proxy z podanej listy.
- Opcjonalna automatyczna rotacja co X sekund **lub** tryb interaktywny.

## 📦 Wymagania

- Python 3.x
- Biblioteka `requests` (można zainstalować przez `pip install requests`)

## 🚀 Uruchomienie

1. Skopiuj lub pobierz plik `ipswitcher.py`.
2. W terminalu uruchom:

```bash
python proxy_switcher.py
