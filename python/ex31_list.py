def show_cart():
    cart = []
    n = int(input("Enter number of items: "))
    for i in range(n):
        item = int(input(f"Enter item {i+1}: "))
        cart.append(item)
    if len(cart) == 0:
        print("Cart is empty")
        return
    print("Shopping Cart Items:")
    for item in cart:
        print(item)

show_cart()