class bankAccount:
    def __init__(self , name, balance):
        self.name = name #public
        self.__balance = balance #private

    def get_balance(self):
        return self.__balance
    
    def set_balance(self , newBalance):
        self.__balance = newBalance
    
R1 = bankAccount("hari",10000)

R1.set_balance(200000)#_bankAccount__balance
print(f"name is {R1.name} and balance is {R1.get_balance()}")

