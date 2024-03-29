class Vehicle:

    def __init__(self, type: str, model: str, price: float, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if self.price <= money and self.owner is None:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif self.price > money:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle)
print(vehicle.buy(35000, "George"))
print(vehicle)
print(vehicle.sell())
print(vehicle.buy(50000, "Peter"))
print(vehicle)
print(vehicle.sell())
print(vehicle.sell())
print(vehicle)
