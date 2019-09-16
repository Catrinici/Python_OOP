# Product Class:
# Attributes:
#   Price
#   Item Name
#   Weight
#   Brand
#   Status: default "for sale"
#   
# Methods:
#   Sell: changes status to "sold"
#   Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
#   Return Item: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20 % discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
#   Display Info: show all product details.
#   Every method that doesn't have to return something should return self so methods can be chained.

class Product:
    def __init__(self,price,name,weight,brand,status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        tax = (10/100) * self.price
        if self.status:
            self.price = self.price + tax
            self.status = "Sold"
        print(self.price)
        print(self.status)
        return self
    
    def reason_for_return(self,reason):

        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if reason == "like_new":
            self.price = self.price + (10/100) * self.price
            self.status = "For Sale"
        if reason == "opened":
            discount = (20/100) * self.price
            self.status = "used"
            self.price = self.price - discount
        return self

    def display_info(self):
        print(f" Product price including Tax fee: {self.price}\n Product Name: {self.name}\n Product Weight: {self.weight} kg\n Product Brand: {self.brand}\n Product Status: {self.status}")
        return self


product1 = Product(100, "Bicycle", 23, "AIST", "For Sale")
product2 = Product(120, "Chair", 23, "Aurora", "For Sale")
product3 = Product(300, "Table", 23, "Florista", "For Sale")
product1.sell()
product1.reason_for_return("opened").display_info()
product2.reason_for_return("like_new").display_info()
product3.reason_for_return("defective").display_info()
