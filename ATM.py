balance = 1000
print("*********************************Welcome to the ATM*******************************")
account_no = int(input("Enter your account number : "))
pin = int(input("Enter your 4 digit security pin : "))
if(account_no <= 1020 and account_no >= 1000 and pin == 9999):
    while True:
        print("\nMenu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            print("\n\nYour balance is ",balance," Rupees\n\n")
            
        elif choice == '2':
            deposit_amount = float(input("Enter the amount to deposit: "))
            balance += deposit_amount
            print("\n\n",deposit_amount," has been deposited. Your new balance is ",balance," Rupees\n\n")
            
        elif choice == '3':
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print("\n\n",withdraw_amount," has been withdrawn. Your new balance is ",balance," Rupees\n\n")
            else:
                print("Insufficient funds")
                
        elif choice == '4':
            print("\n\nThank you for using this ATM. Goodbye!\n\n")
            break
        
        else:
            print("\n\nInvalid choice. Please select a valid option.\n\n")

else:
    print("Wrong Pin or Account number entered")
