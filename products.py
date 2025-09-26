class Product:

    def __init__(self, name: str, price: float, quantity: int = 0, active: bool = True):
        self.name = name
        self.price = price
        self.quantity = 0
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(self.name)
        print(self.price)
        print(self.quantity)

    def buy(self, quantity: int, price: float | None = None) -> int:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.quantity += quantity
        self.price = price
        return self.quantity

#        def sell(self, quantity, price):
#            self.price = price
#            self.quantity -= quantity


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
if __name__ == '__main__':
    main()
