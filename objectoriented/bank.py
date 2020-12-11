class Bank:
    def create_account(self,acno,person_name,balance,bank_name):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance
        self.bank_name=bank_name
    def deposit(self,amount):
        self.balance+=amount
        print("your account",self.acno,"has been credited with amount",amount,"your availale balance:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("your account",self.acno,"balance",self.balance)
        else:
            self.balance-=amount
            print("your account", self.acno, "hasbeen debited with amount",amount,"available  balance",self.balance)
    def balance_enq(self):
        print("your available balance", self.balance)
obj=Bank()
obj.create_account(101,"test",5000,"union")
obj.deposit(1000)
obj.withdraw(500)
obj.balance_enq()
#how to access instant variable outside class
#Instannt variabble--always prepend with self keyword
