import streamlit as st
st.title(" 123 BANK")
class Bank:
   def __init__(self):
       self.acbal = 10000
   def deposit(self):
       try:
           dep = st.number_input("Enter the deposit amount", min_value=1, step=1, key="deposit")

           if dep < 100:
               st.write("Minimum deposit amount should be 100")
           elif dep % 100 != 0:
               st.write("Deposit amount should be multiples of 100")
           elif dep > 50000:
               st.write("Maximum deposit amount should not exceed 50000")
           else:
               self.acbal += dep
               st.write(f"Successfully deposited {dep}. Current Balance: {self.acbal}")
       except ValueError:
           st.write("Invalid numeric input")

   def withdrawl(self):
       for attempt in range(3):
           try:
               wd = st.number_input("Enter the withdrawal amount:", min_value=1, step=1, key=f"withdraw_{attempt}")

               if wd < 100:
                   st.write("Minimum amount to withdraw is 100")
               elif wd % 100 != 0:
                   st.write("The withdrawal amount should be multiples of 100")
               elif wd > self.acbal - 500:
                   st.write("The withdrawal amount is exceeding the account balance")
               elif wd > 20000:
                   st.write("The maximum transaction limit is 20000")
               else:
                   self.acbal -= wd
                   st.write(f"Withdrawal Successfully {wd}. Current Balance: {self.acbal}")
                   break
           except ValueError:
               st.write("Invalid input. Enter a numeric value.")
       else:
           st.write("Maximum transaction attempts reached.")

   def balance_enquiry(self):
       st.write(f"Current Balance: {self.acbal}")

   def view_options(self):
       while True:
           st.write("1. Deposit\n2. Withdrawal\n3. Balance Enquiry\n4. Exit")

           try:
               ch = st.number_input("Enter the choice", min_value=1, step=1, key="option")

               if ch == 1:
                   self.deposit()
               elif ch == 2:
                   self.withdrawl()
               elif ch == 3:
                   self.balance_enquiry()
               elif ch == 4:
                   st.write("Exiting the system")
                   break
               else:
                   st.write("Invalid choice")
           except ValueError:
               st.write("Invalid input.")

   def validate(self):
       for attempt in range(3):
           try:
               pin = st.number_input(f"Enter the pin (Attempt {attempt + 1})", min_value=1, step=1, key=f"pin_{attempt}")

               if pin == 1234:
                   st.write("Successfully Authorized")
                   self.view_options()
                   break
               else:
                   st.write("Invalid pin")
           except ValueError:
               st.write("Invalid input.")
       else:
           st.write("Account blocked due to multiple attempts.")
obj = Bank()
obj.validate()