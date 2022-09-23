from const import ALLOWED_COMMANDS
from function import separator

saldo = 1200.0
store = {}

file = open("store.txt", "w")
file.close()
operation_history = ()

while True:
    separator()
    print(f"Dozwolne komendy: {ALLOWED_COMMANDS}")
    command = input("Wpisz komendę: ")
    command = command.lower()

    if command not in ALLOWED_COMMANDS:
        print("Niepoprawna komenda!")
        continue

    if command == "exit":
        break

    elif command == "konto":
        print(f"Stan konta: {saldo} PLN")
        msg = f"Sprawdzono stan konta. Stan konta: {saldo}"
        with open("store.txt", "a") as file:
            file.write(f"Sprawdzenie stanu konta: {saldo} \n")

    elif command == "magazyn":
        product_name = input("Nazwa towaru: ")

        product_info = store.get(product_name)
        if product_info:
            print(f"Informacje o produkcie: {product_name}")
            print(product_info)
        else:
            print(f"Nie ma towaru '{product_name}' w magazynie!")
        msg = f"Sprawdzono stan magazynu dla produktu {product_name}."
        with open("store.txt", "a") as file:
            file.write(f"Sprawdzenie stanu magazynu: {product_name} \n")

    elif command == "zakup":
        product_name = input("Nazwa produktu: ")
        price = input("Cena za sztukę: ")
        try:
            price = float(price)
        except ValueError:
            print("Prosze podawac tylko liczby! ")
            continue

        count = input("Ilość: ")
        if count.isnumeric():
            count = int(count)
        else:
            print("Prosze podawac tylko liczby! ")
            continue
        product_total_price = price*count

        if product_total_price > saldo:
            print(f"Za mało środków na koncie ({saldo}) na zakup towarów za cenę {product_total_price}!")
            continue
        else:
            saldo -= product_total_price
            if product_name in store.keys():
                store[product_name]["price"] = price
                store[product_name]["count"] += count
            else:
                store[product_name] = {"price": price, "count": count}
                msg = f"Zakupiono product {product_name}. Ilosc sztuk: {count}. Za kwote {price} PLN. "
                with open("store.txt", "a") as file:
                    file.write(f"zakup: {product_name}, {price}, {count}\n")

    elif command == "saldo":
        price = input("Kwota zmiany salda: ")
        try:
            price = float(price)
        except ValueError:
            print("Prosze podawac tylko liczby! ")
            continue
        price = float(price)
        koment = input("Komentarz: ")
        if (saldo + price) >= 0:
            saldo += price
        else:
            print("Brak wystarczających środków na koncie!")
            continue
        msg = f"Operacja na saldzie, nowe saldo po operacji = {saldo}. Komentarz: {koment}. Ile: {price} PLN"
        with open("store.txt", "a") as file:
            file.write(f"Operacja na saldzie, nowe saldo po operacji = {saldo}. Komentarz: {koment}. Ile: {price} PLN\n")

    elif command == "sprzedaz":
        product_name = input("Nazwa produktu: ")

        if product_name not in store:
            print(f"Nie ma takiego produktu w magazynie!")
        else:
            if product_name in store.keys():
                count = input("Ilość: ")
                try:
                    count = float(count)
                except ValueError:
                    print("Prosze podawac tylko liczby! ")
                    continue
                price = store[product_name]["price"]
                ilosc_w_magazynie = store[product_name]["count"]
                price = float(price)
                count = int(count)

                if count > ilosc_w_magazynie:
                    print(f"Niewystarczajaca ilosc {product_name} w magazynie! ")
                    continue
                total_price = price * count

                saldo += total_price
                if product_name in store.keys():
                    store[product_name]["count"] -= count
                    msg = f"Sprzedano product {product_name}. Ilosc sztuk: {count}. Za kwote {total_price} PLN. "
                    with open("store.txt", "a") as file:
                        file.write(f"Sprzedano product {product_name}. Ilosc sztuk: {count}. Za kwote {total_price} PLN.\n")

    elif command == "przeglad":
        start = input("Od: ")
        end = input("Do: ")
        with open("store.txt") as file:
            if start == '' and end == '':
                for line in file.readlines():
                    print(line.replace("\n", ""))
            elif start != '' and end == '':
                for line in file.readlines()[int(start):]:
                    print(line.replace("\n", ""))
            elif start == '' and end != '':
                for line in file.readlines()[:int(end)]:
                    print(line.replace("\n", ""))
            else:
                for line in file.readlines()[int(start):int(end)]:
                    print(line.replace("\n", ""))
