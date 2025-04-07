import json
import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            global tasks
            tasks = json.load(file)

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_menu():
    print("\n=== MÓJ ASYSTENT ZADAŃ ===")
    print("1. Dodaj zadanie")
    print("2. Pokaż listę zadań")
    print("3. Oznacz zadanie jako wykonane")
    print("4. Wyjdź")

def add_task():
    tekst = input("Wpisz treść zadania: ")
    deadline = input("Wpisz deadline (YYYY-MM-DD): ")
    kategoria = input("Wpisz kategorię (np. praca/dom/zdrowie): ")
    tasks.append({
        "tekst": tekst,
        "zrobione": False,
        "deadline": deadline,
        "kategoria": kategoria
    })
    print("✅ Zadanie dodane!")
    save_tasks()

def show_tasks():
    if not tasks:
        print("📭 Lista zadań jest pusta.")
    else:
        print("\n📝 Twoje zadania:")
        for i, task in enumerate(tasks):
            status = "[X]" if task.get("zrobione") else "[ ]"
            tekst = task.get("tekst", "Brak treści")
            deadline = task.get("deadline", "brak daty")
            kategoria = task.get("kategoria", "brak kategorii")

            print(f"{i+1}. {status} {tekst} | 📅 {deadline} | 🗂️ {kategoria}")

def complete_task():
    show_tasks()
    try:
        number = int(input("Wpisz numer zadania do oznaczenia jako wykonane: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["zrobione"] = True
            print("🎉 Zadanie oznaczone jako wykonane.")
            save_tasks()
        else:
            print("⚠️ Nieprawidłowy numer.")
    except ValueError:
        print("❗ Podaj prawidłowy numer.")

# 🔁 Główna pętla
load_tasks()

while True:
    print("🔄 Pętla działa...")
    show_menu()
    choice = input("Wybierz opcję (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("👋 Do zobaczenia!")
        break
    else:
        print("⚠️ Nieznana opcja, spróbuj ponownie.")


