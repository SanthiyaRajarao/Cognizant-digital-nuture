class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        total = sum(item.total_price() for item in self.items)
        gst = total * 0.18
        final_total = total + gst
        return total, gst, final_total

    def print_receipt(self):
        print("\n--- Receipt ---")
        for item in self.items:
            print(item.name, "-", item.quantity, "x", item.price, "=", item.total_price())

        total, gst, final_total = self.calculate_total()

        print("\nTotal:", total)
        print("GST (18%):", gst)
        print("Final Total:", final_total)


def main():
    cart = ShoppingCart()

    cart.add_item(CartItem("Rice", 50, 2))
    cart.add_item(CartItem("Milk", 30, 3))
    cart.add_item(CartItem("Soap", 40, 1))

    cart.remove_item("Soap")

    cart.print_receipt()


main()