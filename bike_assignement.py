class Bike:

    def __init__(self, price, max_speed, miles):
       self.price = price
       self.max_speed = max_speed
       self.miles = abs(0)


    def ride(self):
        print("Riding!")
        self.miles += 10
        print(f"Total miles : {self.miles}")
        return self

    def reverse(self):
        print("Reversing!")
        self.miles -= 5
        print(f"Total miles : {abs(self.miles)}")
        return self

    def displayInfo(self):
        print(
            f"The price of this bike is ${ self.price }. The maximum speed is {self.max_speed}.Total riding miles is: {abs(self.miles)} miles")
        return self

# Have the first instance ride three times, reverse once and have it displayInfo().
bike1 = Bike(200,"24mph",0)
i = 1
while i <=3:
    bike1.ride()
    i+=1

bike1.reverse().displayInfo()


# Have the second instance ride twice, reverse twice and have it displayInfo().
bike2 = Bike(150,"20mph",0)
i = 1
while i <=2:
    bike2.ride().reverse()
    i+=1
bike2.displayInfo()


# Have the third instance reverse three times and displayInfo().
bike3 = Bike(110,"18mph",0)
i = 1
while i <=3:
    bike3.reverse()
    i+=1
bike3.displayInfo()

