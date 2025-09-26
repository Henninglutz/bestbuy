#initaliziation of products by using class (OOP)
class Product:
    def __init__(self, name: str, price: float, quantity: int = 0, active: bool = True):
        if price < 0:
            raise ValueError("Price must be non-negative")
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = bool(active)

#buitin function
    def __str__(self) -> str:
        status = "active" if self.active else "inactive"
        return f"{self.name} | price: {self.price} | qty: {self.quantity} ({status})"

#getter of quantity
    def get_quantity(self) -> int:
        return self.quantity

#setter of qty
    def set_quantity(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity must be >= 0")
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.active = False

#status of active / deactivate
    def is_active(self) -> bool:
        return self.active

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

#storeage and validation of collection
    def buy(self, quantity: int, price: float | None = None) -> int:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if price is not None:
            if price < 0:
                raise ValueError("Price must be non-negative")
            self.price = float(price)
        self.quantity += int(quantity)
        if self.quantity > 0:
            self.active = True
        return self.quantity

#decrease qty after sale
    def sell(self, quantity: int) -> int:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError(f"Not enough '{self.name}' in stock (have {self.quantity})")
        self.quantity -= int(quantity)
        if self.quantity == 0:
            self.active = False
        return self.quantity