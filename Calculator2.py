atm_data = {
    'Pin': '9999',
}
balance = 1000

print("********************************* Welcome to the ATM *******************************")
account_no = int(input("Enter your account number : "))
if(account_no <= 1020 and account_no >= 1000 ):
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change password")
        print("5. Exit")

        choice = input("Please select an option (1/2/3/4/5): ")
        
        if choice == '4':
            pin = str(input("Enter your current pin: "))
            if pin == atm_data['Pin']:
                x = input("Enter your new password: ")
                atm_data['Pin'] = x
                print("Password changed successfully.")
            else:
                print("Incorrect password.")
            
        elif choice == '1':
            print("\n\nYour balance is ",balance," Rupees\n\n")
            
        elif choice == '2':
            pin = str(input("Enter your 4 digit security pin : "))
            if(pin == atm_data['Pin'] ):
                deposit_amount = float(input("Enter the amount to deposit: "))
                balance += deposit_amount
                print("\n\n",deposit_amount," has been deposited. Your new balance is ",balance," Rupees\n\n")
            else:
                print("Wrong pin")
            
        elif choice == '3':
            pin = str(input("Enter your 4 digit security pin : "))
            if(pin == atm_data['Pin'] ):
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount

                    sum = 0
                    while(True):
                        if sum >= withdraw_amount:
                            break
                        else:
                            currency = int(input("Please choose the currency note : 2000\n500\n100\n"))
                            print("Enter the count of",currency,"Rupee notes :")
                            count = int(input())
                            sum += currency*count
                            print(count,currency,"rupee notes")
                    print("\n\n",withdraw_amount," has been withdrawn. Your new balance is ",balance," Rupees\n\n")

                else:
                    print("Insufficient funds")
            else:
                print("Wrong pin")
                
        elif choice == '5':
            print("\n\nThank you for using this ATM. Goodbye!\n\n")
            break
        
        else:
            print("\n\nInvalid choice. Please select a valid option.\n\n")

else:
    print("Wrong Pin or Account number entered")
