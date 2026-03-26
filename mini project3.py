
cart = [
    {"name": "Apple", "price": 50, "quantity": 2},
    {"name": "Milk", "price": 30, "quantity": 1},
    {"name": "Bread", "price": 40, "quantity": 3},
    {"name": "Eggs", "price": 6, "quantity": 12}
]

def display_cart():
    if len(cart) == 0:
        print("Cart is empty.\n")
        return

    print("\n Shopping Cart:")
    total = 0

    for item in cart:
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]
        subtotal = price * quantity
        total += subtotal

        print(f"Name: {name} | Price: {price} | Quantity: {quantity} | Subtotal: {subtotal}")

    print(f"Total Bill: {total}\n")



display_cart()