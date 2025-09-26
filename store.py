from typing import List, Tuple
from products import Product

#initalization of OOP class
class Store:
    def __init__(self, products: List[Product] | None = None):
        self._products: List[Product] = list(products) if products else []


#adding products which are not yet listed
    def add_product(self, product: Product) -> None:
        if product not in self._products:
            self._products.append(product)


#delete products from store inventory
    def remove_product(self, product: Product) -> None:
        if product in self._products:
            self._products.remove(product)

#sum of availabe products
    def get_total_quantity(self) -> int:
        return sum(p.quantity for p in self._products if p.is_active())

# lists all active products
    def get_all_products(self) -> List[Product]:
        return [p for p in self._products if p.is_active()]


#checks order validation
    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        if not shopping_list:
            raise ValueError("Empty order")

# is product available
        for product, qty in shopping_list:
            if product not in self._products:
                raise ValueError(f"Product '{getattr(product, 'name', '?')}' not listed.")
            if not product.is_active():
                raise ValueError(f"Product '{product.name}' not active.")
            if qty <= 0:
                raise ValueError(f"Quantity must be > 0 for '{product.name}'.")
            if qty > product.get_quantity():
                raise ValueError(
                    f"Not enough '{product.name}': available {product.get_quantity()}."
                )

# total price?
        total_price = 0.0
        for product, qty in shopping_list:
            total_price += product.price * qty

# amount ?
        for product, qty in shopping_list:
            product.sell(qty)
        return float(total_price)
