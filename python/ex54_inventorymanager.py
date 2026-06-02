#(OOP + Inheritance + Dictionaries + Sets)
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        return f"{self.name} | Price: {self.price} | Stock: {self.stock}"


class Perishable(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.expiry_date = expiry_date


class Electronics(Product):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years


class InventoryManager:
    def __init__(self):
        self.products = {}
        self.low_stock_alert = set()

    def add_product(self, product):
        self.products[product.name] = product

        if product.stock < 5:
            self.low_stock_alert.add(product.name)

    def update_stock(self, name, new_stock):
        if name in self.products:
            self.products[name].stock = new_stock

            if new_stock < 5:
                self.low_stock_alert.add(name)
            elif name in self.low_stock_alert:
                self.low_stock_alert.remove(name)

    def show_inventory(self):
        print("\n--- Inventory ---")
        for product in self.products.values():
            print(product.display())

    def show_low_stock(self):
        print("\n--- Low Stock Items ---")
        for item in self.low_stock_alert:
            print(item)


def main():
    manager = InventoryManager()

    p1 = Perishable("Milk", 50, 3, "2026-06-10")
    p2 = Electronics("Phone", 15000, 10, 2)
    p3 = Product("Book", 200, 2)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    manager.show_inventory()
    manager.show_low_stock()

    manager.update_stock("Phone", 3)

    print("\nAfter Update:")
    manager.show_inventory()
    manager.show_low_stock()


main()