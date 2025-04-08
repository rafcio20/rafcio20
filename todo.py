def wyswietl_menu():
    print("\nTo-Do List")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Usuń zadanie")
    print("4. Wyjście")

def dodaj_zadanie(lista):
    zadanie = input("Podaj treść zadania: ")
    lista.append(zadanie)
    print("Dodano zadanie!")

def wyswietl_zadania(lista):
    if not lista:
        print("Brak zadań na liście.")
    else:
        print("\nLista zadań:")
        for i, zadanie in enumerate(lista, 1):
            print(f"{i}. {zadanie}")

def usun_zadanie(lista):
    wyswietl_zadania(lista)
    try:
        indeks = int(input("Podaj numer zadania do usunięcia: ")) - 1
        if 0 <= indeks < len(lista):
            usuniete = lista.pop(indeks)
            print(f"Usunięto zadanie: {usuniete}")
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Podaj poprawny numer.")

def main():
    lista_zadan = []
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            dodaj_zadanie(lista_zadan)
        elif wybor == "2":
            wyswietl_zadania(lista_zadan)
        elif wybor == "3":
            usun_zadanie(lista_zadan)
        elif wybor == "4":
            print("Do zobaczenia!")
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()