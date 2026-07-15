import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8,
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
}

def check_winnings(colums,lines,bets,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol !=symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line+1)
        return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol.count):
            all_symbols.append(symbol)

        columns = []
        for _ in range(cols):
            columns = []
            column_synbols = all_symbols[:]
            for _ in range (rows):
                value = random.choice(current.symbols)
                current.symbols.remove(value)
                columns.append(value)

            columns.append(column)
        return columns

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = "|" )
            else:
                print(column[row],end = "")

            print()

def deposit():
    while True:
        amount = input("What would  you like to deposit?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please Enter  a number")
    return amount

