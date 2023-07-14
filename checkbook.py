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
    bal = balance
    return bal

while True:
    
    print('~~~Welcome to your terminal checkbook!~~~')

    print()

    menu = int(input(''' What would you like to do?

1) view current balance
2) record a debit (withdraw)
3) record a credit (deposit)
4) exit

Your choice? '''))

    print()

    if menu == 1:
        
        balance = float(total_balance(balance))
        
        print(f' Your current balance is: ${balance}')

    elif menu == 2:
        
        w = int(input('How much would you like to withdraw? '))
          
        balance = float(withdraw(w))
         
        print(f'New balance: ${balance}')

    elif menu == 3:

        d = int(input('How much would you like to deposit? '))
        
        balance = float(deposit(d))

        print(f'New balance: ${balance}')

    elif menu == 4:
        
        with open ('checkbook.json', 'w') as f:
            json.dump(balance, f)
        
        print('Thanks, have a great day!')
        
        break

    else: 
    
        print(f'invalid: {menu}')

        