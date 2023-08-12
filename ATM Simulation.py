# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:04:52 2023

@author: PC
"""


print('Welcome to ABC Bank of Nigeria, we are here to serve you 247')
restart = ('Y')
chances = 3
balance = 3500


while chances >= 0:
    userInfo = {'Account Number' : 1234567890,
                'Pin' : 12345
        }  #acct number and the pin are saved here using concept of dictionary             
    while True:
        print('you entered your info correctly')
        while restart not in ('n', 'No', 'no', 'N'): # concept of tuple
            print('Please Press 1 For Your Balance')
            print('please Press 2 To Make a Withdrawal')
            print('Please Press 3 To Pay In') 
            print('Please, Press 4 To Return Card')
            
            option = int(input('What would you like to choose'))
            if option == 1:
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawal = float(input('How much would you like to withdraw?'))
                if withdrawal in [1000, 2000, 5000, 10000]:
                    balance = balance - withdrawal
                    print('Your balance is ' +str(balance))
                    restart = input('would your like to go back?')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank you')
                        break
                elif withdrawal != [1000, 2000, 5000, 10000]:
                    print('Invalid Amount, Please Re-try')
                    restart = ('y')
                elif withdrawal == 1:
                    withdrawal = float(input('Please, Enter Desired Amount'))
            elif option == 3:
                payIn = float(input('How much would you like to pay in?'))
                balance = balance + payIn
                print('Your balance is now , balance')
                restart = input('Would you like to go back?')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option ==4:
                print('Please wait while your card is returned...')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct uerInfo.')
                restart = ('y')
        elif userInfo != {'Account Number' : 1234567890,
                    'Pin' : 12345
                    }:
            print('incorrect account number and pin')
            chances = chances - 1
            if chances == 0: 
                print('No more tries')
                break
            
                    
                    
                    