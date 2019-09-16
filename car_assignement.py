class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
        
    
    def display_all(self):
        tax = 12
        if self.price > 10000:
            tax = 15
        print(f" Price:{self.price} \n Speed:{self.speed}\n Fuel:{self.fuel}\n Mileage:{self.mileage}\n Tax:{tax}% ")
    

        
car1 = Car(2000,"35mph","Full","15mpg")
car2 = Car(11000,"40mph","Full","19mpg")
print(car1.price)
car1.display_all()
car2.display_all()

