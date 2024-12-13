class bank:
    def __init__(self):
        self.acbal = 10000

    def deposit(self):
        try:
            dep = int(input("Enter the deposit amount"))

            if dep < 100:
                print("Minimum deposit amount should be 100")
            elif dep % 100 != 0:
                print("Deposit amount should be multiples of ")
            elif dep > 50000:
                print("Maximum deposit amount should not exceed 50000")
            else:
                self.acbal += dep
                print(f"Successfully deposited {dep}.Current Balance:{self.acbal}")
        except ValueError:
            print("Invalid numeric ")

    def withdrawl(self):
        for attempt in range(3):
            try:
                wd = int(input("Enter the withdrawl amount:"))
                if wd < 100:
                    print("Minimum amount to withdraw is 100")
                elif wd % 100 != 0:
                    print("The withdrawl amount should be multiples of 100")
                elif wd > self.acbal - 500:
                    print("The withdrawl amount is exceeding the account balance")
                elif wd > 20000:
                    print("The maximum transaction limit is 20000")
                else:
                    self.acbal -= wd
                    print(f"Withdrawl Successfully {wd}.Current Balance:{self.acbal}")
                    break
            except ValueError:
                print("Invalid input.Enter the numeric input")
        else:
            print("Maximum transactions limit reached")

    def balance_enquiry(self):
        print(f"Current Balance:{self.acbal}")

    def view_options(self):
        while True:
            print("1.Deposit\n2:Withdrawl\n3.Balance Enquiry\n4.Exit")

            try:
                ch = int(input("Enter the choice"))
                if ch == 1:
                    self.deposit()
                elif ch == 2:
                    self.withdrawl()
                elif ch == 3:
                    self.balance_enquiry()
                elif ch == 4:
                    print("Exiting the system")
                    break
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid input.")

    def validate(self):
        for attempt in range(3):
            try:
                pin = int(input("Enter the pin "))

                if pin == 1234:
                    print("Successfuly Authorized")
                    self.view_options()
                    break
                else:
                    print("Invalid pin")
            except ValueError:
                print("Invalid input ")
        else:
            print("Account blocked due to multiple attempts")


obj = bank()
obj.validate()