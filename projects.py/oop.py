class Smartphone:
    """A class representing a smartphone."""

    def __init__(self, brand, model, color, storage):
        """Constructor to initialize a Smartphone object.

        Args:
            brand (str): The brand of the smartphone (e.g., Apple, Samsung).
            model (str): The model of the smartphone (e.g., iPhone 14, Galaxy S23).
            color (str): The color of the smartphone (e.g., Black, White, Gold).
            storage (int): The storage capacity of the smartphone in GB.
        """
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage
        self.battery = 100  # Initial battery level

    def make_call(self, number):
        """Simulates making a phone call."""
        print(f"Calling {number} from {self.brand} {self.model}")

    def send_message(self, recipient, message):
        """Simulates sending a text message."""
        print(f"Sending message to {recipient}: {message}")

    def check_battery(self):
        """Checks the current battery level."""
        print(f"Battery level: {self.battery}%")

    def charge(self, minutes):
        """Simulates charging the smartphone."""
        charging_rate = 2  # Charging rate in percentage per minute
        self.battery = min(self.battery + (charging_rate * minutes), 100)
        print(f"Charged for {minutes} minutes. Battery level: {self.battery}%")

# Example usage
my_phone = Smartphone("Apple", "iPhone 14", "Black", 256)
my_phone.make_call("123-456-7890")
my_phone.send_message("Friend", "Hello!")
my_phone.check_battery()
my_phone.charge(30) 




class Animal:
    """Base class for animals."""

    def move(self):
        """Abstract method for movement."""
        raise NotImplementedError("Subclasses must implement move()")

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

class Car(Animal): 
    def move(self):
        print("Driving")

class Plane(Animal): 
    def move(self):
        print("Flying")

# Example usage
dog = Dog()
bird = Bird()
fish = Fish()
car = Car()
plane = Plane()

dog.move()  
bird.move()
fish.move()  
car.move()  
plane.move()  


class Animal:
    """Base class for animals."""

    def move(self):
        """Abstract method for movement."""
        raise NotImplementedError("Subclasses must implement move()")

class Dog(Animal):
    def move(self):
        print("Running")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

class Car(Animal): 
    def move(self):
        print("Driving")

class Plane(Animal): 
    def move(self):
        print("Flying")

# Example usage
dog = Dog()
bird = Bird()
fish = Fish()
car = Car()
plane = Plane()

dog.move()  
bird.move()  
fish.move()  
car.move()  
plane.move()  