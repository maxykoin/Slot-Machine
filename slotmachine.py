from random import *


LINES = 3
ROWS = 3
COLS = 3


csymbols = {
    "A": randint(2, 5),
    "B": randint(2, 6),
    "C": randint(2, 7),
    "D": randint(2, 8)
}

symvalues = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def spinslot(rows, cols, symbols):
    allsymbols = []
    for symbol, csymbols in symbols.items():
        for _ in range(csymbols):
            allsymbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current = allsymbols[:] 
        for _ in range(rows):
            value = choice(current) # choice not choices as i learned after 40 minutes of trying to figure out why it didn't work
            if value in current:
                current.remove(value)
                column.append(value)
            else:
                print('Error')
        columns.append(column)
    return columns
    
    
def printslot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ") 
        print()  


def deposit():
    while True:
        try: 
            amount = int(input('What would you like to deposit? $'))
            if amount <= 0:
                    print('Invalid value')
            else:
                break
        except:
            print('Invalid value')
    return amount


def nlines():
    while True:
        try:
            clines = int(input(f'Enter the numbers of line to bet on (1-{LINES}) '))
            if clines > LINES:
                print('Invalid value')
            elif clines <= 0:
                print('Invalid value')
            else:
                break
        except:
            print('Invalid value')
    return clines


def bets():
    while True:
        try:
            cbet = int(input(f'How much would you like to bet on each line? $'))
            if cbet <= 0:
                    print('Invalid value')
            else:
                break
        except:
            print('Invalid value')
    return cbet


def winning(columns, lines, bet, values):
    winnings = 0
    winlines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            check = column[line]
            if symbol != check:
                break
        else:
            winnings += values[symbol] * bet
            winlines.append(line + 1)
            
    return winnings, winlines

def spin(balance):
    lines = nlines()
    while True: 
        bet = bets()
        totalbet = bet * lines
        if totalbet > balance:
            print(f"You don't have enough money for this bet, your balance is ${balance}")
        else:
            break
        
    print(f"""You're betting ${bet} on {lines} line(s).
    Your total bet is: ${totalbet}""")
    
    slots = spinslot(ROWS, COLS, csymbols)
    printslot(slots)
    winnings, winlines = winning(slots, lines, bet, symvalues)
    print(f"You won ${winnings} on line", *winlines)
    return winnings - totalbet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        play = input('Press enter to play (Q to quit) ').upper()
        if play == "Q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()