# 📡 Mini Centrum Dowodzenia (Python CLI)

Terminalowe narzędzie diagnostyczne, które pokazuje podstawowe informacje o Twoim połączeniu sieciowym — idealne do nauki działania IP, lokalizacji, VPN/proxy i podstaw monitorowania połączeń.

## 🔧 Funkcje

- ✅ Sprawdzanie połączenia z internetem
- 🌍 Pobieranie **zewnętrznego adresu IP** (`ipify.org`)
- 🏠 Pobieranie **lokalnego IP**
- 📍 Określanie lokalizacji IP przez API (`ip-api.com`)
- 🛡️ Detekcja działania **VPN lub proxy** (porównanie IP)
- 🔁 Automatyczne odświeżanie informacji co 15 sekund

## 📦 Wymagania

- Python 3.x
- Biblioteki:
  - `requests`
  - `psutil` (opcjonalnie — do rozbudowy)

Zainstaluj je poleceniem:
```bash
pip install requests psutil
