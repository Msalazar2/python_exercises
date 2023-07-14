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
        
        balance = round(float(total_balance(balance)), 2)
        
        print(f' Your current balance is: ${balance}')

    elif menu == 2:
        
        w = float(input('How much would you like to withdraw? '))
          
        balance = round(float(withdraw(w)), 2)
         
        print(f'New balance: ${balance}')

    elif menu == 3:

        d = float(input('How much would you like to deposit? '))
        
        balance = round(float(deposit(d)), 2)

        print(f'New balance: ${balance}')

    elif menu == 4:
        
        with open ('checkbook.json', 'w') as f:
            json.dump(balance, f)
        
        print('Thanks, have a great day!')
        
        break

    else: 
    
        print(f'invalid: {menu}')

        