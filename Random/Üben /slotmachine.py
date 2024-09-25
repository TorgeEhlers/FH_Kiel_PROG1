import random 

MAX_LINIEN = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


def spin_der_slotmachine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def einzahlen():
    while True:
        anzahl = input("Wie viel wollen sie einzahlen: ")
        if anzahl.isdigit():
            anzahl = int(anzahl)
            if anzahl > 0:
                break
            else:
                print("Die Anzahl muss größer als 0 sein!")
        else:
            print("Bitte gebe eine Nummer ein")
    
    return anzahl

def anzahl_der_linien():
    while True:
        linien = input("Auf wie viele Linien wollen sie setzen? (1- " + str(MAX_LINIEN)+ ")? ")
        if linien.isdigit():
            linien = int(linien)
            if 1 <= linien <= MAX_LINIEN:
                break
            else:
                print("Gib eine richtige Anzahl an Linien ein!")
        else:
            print("Bitte gebe eine Nummer ein")
    
    return linien

def wette_setzen():
    while True:
        anzahl = input("Wie viel wollen sie auf jede Linie setzen: ")
        if anzahl.isdigit():
            anzahl = int(anzahl)
            if MIN_BET <= anzahl <= MAX_BET:
                break
            else:
                print(f"Die Anzahl muss zwischen {MIN_BET} und {MAX_BET} liegen!")
        else:
            print("Bitte gebe eine Nummer ein")
    
    return anzahl


def spin(balance):
    linien = anzahl_der_linien()
    while True: 
        wette = wette_setzen()
        insgesamte_wette = wette * linien
    
        if insgesamte_wette > balance:
            print("Du hast nicht genug eingezahlt, um eine so hohe Summe zu setzen!")
        else:
            break

    print(f"Du setzt {wette}€ auf {linien} Linien! Insgesamt setzt du {insgesamte_wette}€!")

    slots = spin_der_slotmachine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, linien, wette, symbol_value)
    print(f"Du hast {winnings}€ gewonnen!")
    print(f" Du hast gewonnen auf:", *winnings_lines, "Linien")
    return winnings - insgesamte_wette


def main():
    balance = einzahlen()
    while True:
        print(f"Current balance is: {balance} ")
        answer = input("Drücke Enter zum weiter spielen (q zum aufhören).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Du hast noch: {balance}€ ")


main()
