import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = store.Store(product_list)

#checks inventory and returns a info for the user by calling get_all_products()
def _list_products(store_obj: store.Store) -> None:
    product_list = store_obj.get_all_products()
    if not product_list:
        print("No products available.")
        return
    for idx, p in enumerate(product_list, start=1):
        print(f"{idx}. {p.name} | price: {p.price} | qty: {p.quantity}")

#checks the qty by calling the function get_total_quantity()
def _show_total_amount(store_obj: store.Store) -> None:
    total = store_obj.get_total_quantity()
    print(f"Total amount in store: {total}")


#information about the input
def _make_order(store_obj: store.Store) -> None:
    print("Enter order as 'product name, quantity'. or hit 'Enter' to cancel (empty line).")
    order_list = []

    line = input("> ").strip()
    if line == "":
        print("No items to order.")
        return

# validation of user input name and qty
    if "," not in line:
        print("Please use the format: product name, quantity")
        return
    name_part, qty_part = line.split(",", 1)
    name = name_part.strip().lower()
    qty_str = qty_part.strip()

    try:
        qty = int(qty_str)
    except ValueError:
        print("Quantity must be an integer.")
        return
    if qty <= 0:
        print("Quantity must be positive.")
        return

#search for product
    product = None
    for p in store_obj.get_all_products():
        if p.name.lower() == name.lower():
            product = p
            break
    if product is None:
        for p in store_obj.get_all_products():
            if p.name.lower().startswith(name):
                product = p
                break
        print("Product not found.")
        return

    order_list.append((product, qty))

# make order
    try:
        total = store_obj.order(order_list)
        print(f"Order placed. Total price: {total}")
    except Exception as e:
        print(f"Order failed: {e}")


#shows the menu and calls the funtion
def start(store_obj: store.Store) -> None:
    while True:
        print("\n1. List all products in the store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            _list_products(store_obj)
        elif choice == "2":
            _show_total_amount(store_obj)
        elif choice == "3":
            _make_order(store_obj)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please enter 1–4.")


if __name__ == "__main__":
    start(best_buy)