import products
from products import Product


class Store:
    def __init__(self, products):
        self._products = list[Product]()

    def add_product(self, product):
        if product not in self._products:
            self._products.append(product)

    def remove_product(self, product):
        if product in self._products:
            self._products.remove(product)

    def get_total_quantity(self) -> int:
        for p in self._products:
            if p.is_active():
                all_products += p.quantity
            return sum(all_products)


    def get_all_products(self) -> list[Product]:
        for p in self._products:
            if p.is_active():
                return [p.quantity]

    def order(self, shopping_list) -> float:
        for product, qty in shopping_list:
            if product not in self._products:
                raise ValueError(f"Product '{product, 'name', '?'}' not listed.")
            if not product.is_active():
                raise ValueError(f"Product '{product.name}' not active.")
            if qty <= 0:
                raise ValueError(f"try an other quantity, less than {qty} for '{product.name}'.")
            if qty > product.get_quantity():
                raise ValueError(
                    f"not enough '{product.name}': "
                    f"available: {product.get_quantity()}."
                )

                # 2) Preis berechnen (aktueller Produktpreis * Menge)
            total_price = 0.0
            for product, qty in shopping_list:
                total_price += product.price * qty

            # 3) Verkauf durchführen (Bestand reduzieren)
            for product, qty in shopping_list:
                product.sell(qty)

            return float(total_price)

bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

best_buy = Store([bose, mac])

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy.add_product(pixel)