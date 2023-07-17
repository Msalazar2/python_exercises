import json
import os

with open ('checkbook.json', 'r') as f:
    balance = json.load(f)
    
def withdraw(debit):
    debit = balance - debit
    return debit

def deposit(credit):
    credit += balance
    return credit

def total_balance(bal):
    bal = credit - debit
    return bal2

def transactions(t):
    history = []
    t = balance
    history += t
    return history


while True:
    
    print('~~~Welcome to your terminal checkbook!~~~')

    print()

    print('1) view current balance')
    print('2) record a debit (withdraw)')
    print('3) record a credit (deposit)')
    print('4) history')
    print('5) exit')

    print()

    menu = input('What would you like to do? ')

    print()

    confirm = input(f'Your choice? {menu}')

    print()



    if menu.strip() == '1':
        
        print(f'current balance: {balance}')

    elif menu.strip() == '2':
        
        w = int(input('How much would you like to withdraw? '))
          
        balance = withdraw(w)
         
        print(f'total debit: {balance}')

    elif menu.strip() == '3':

        d = int(input('How much would you like to deposit? '))
        
        balance = deposit(d)

        print(f'total credit {balance}')
        
    elif menu.strip() == '4':
        
        transactions = transactions(balance)
        
        print(transactions)

    elif menu.strip() == '5':
        
        with open ('checkbook.json', 'w') as f:
            json.dump(balance, f)
        
        print('Thanks, have a great day!')
        
        break

    else: 
    
        print(f'invalid: {menu}')