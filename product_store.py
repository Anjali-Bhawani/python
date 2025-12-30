class Products:
    count = 0
    store_place = "flipkart"

    def __init__(self , name , price , company):
        self.name = name
        self.price = price
        self.company = company
        Products.count += 1

    def get_info(self):
        print(f"product is {self.name} with price range of {self.price} and of {self.company} company")   

    @staticmethod
    def calc_discount(price , discount):
        final_price = price - (discount * price / 100)
        print(f"final price after discount is = {final_price}")

    @classmethod
    def get_total_count(cls):
        print(f"total number of products is {cls.count}")

cello = Products('pen','10','mark')
poco = Products("mobile","30000","samsung")
Realme = Products("mobile","40000","MI")
cello.get_info()
cello.calc_discount(50000 , 10)

Products.get_total_count()
