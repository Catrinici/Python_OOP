class Animal:
    def __init__(self,name,health):
        self.name = name
        self.health = 150

    def walk(self):
        print("Animal has walked")
        self.health -=1
        return self
    
    def run(self):
        print("Animal has runned")
        self.health -=5
        return self
    
    def display_health(self):
        print(f"I am a {self.name}! My current health condition is: {self.health}")
        return self

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.health = 150
    
    def pet(self):
        self.health += 5

class Dragon(Animal):
    def __init__(self):
        super().__init__()
        self.health = 170

    def fly(self):
        self.health -= 10



# dog1 = Animal("boba", 150)

# dog1.walk().walk().walk().run().run().pet().display_health()
