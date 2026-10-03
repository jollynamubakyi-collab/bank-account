class BankAccount:
    def__init__(self,account_holder,intial_balance=0.0):
        self.account_holder= account_holder
        self.intial_balance=intial_balance
    

    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount must be positive..")
        else
            self.balance=amount=
            print("Deposited ${amount:2f}.New Balance:${self.balance:2f}")

    def  withdraw(self,amount):
        if amount<=0:
            print("withdraw amount must be positive.")
        elif amount>self.balance:
            print(f"insufficient funds! current balance:$(self.balance:.2f")
         else:
            self.balance= amount
            print(f"withdraw ${amount:.2f}.New balance:${self.balance:.}") 

      def display_account_info(self)
          print(f"Account holder:{self.account_holder},current balance:${self.balance:.2f}")

          Print("Testing Account 1(Alice)")
          account1= BankAccount("Alice,"100,00)
          account1=.deposit(5000)
          account1=.withdraw(30000)
          account1=.display_account_info()



          print("Testing Account 2(Bob)")
          account2=BankAccout("Bob")
          account2.deposit(-1000)
          account2.deposit(7500)
          account2.display_account_info()     
                                   

    