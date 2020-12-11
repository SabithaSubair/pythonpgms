class Bank:
    # #static declaration
    # @staticmethod
    # def utility_method():#nothing related to object
    #     print("utility method")
    #class method
    @classmethod
    def change_bank_name(cls):
        cls.bank_name("SBI")
    bank_name="sbk"
    def create_account(self,acno,person_name,balance):
        self.acno=acno
        self.person_name=person_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(Bank.bank_name,"your account",self.acno,"has been credited with amount",amount,"your availale balance:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("your account",self.acno,"balance",self.balance)
        else:
            self.balance-=amount
            print("your account", self.acno, "hasbeen debited with amount",amount,"available  balance",self.balance)
    def balance_enq(self):
        print("your available balance", self.balance)
obj=Bank()
obj.create_account(101,"test",5000)
obj.deposit(1000)
obj.withdraw(200)
obj.balance_enq()
#Bank.utility_method()
Bank.change_bank_name()
print(Bank.bank_name)

