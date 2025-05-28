class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"- {self.name} (${self.price:.2f}, Qty: {self.quantity})")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"\nProduct '{name}' added successfully!")

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def update_quantity(self, name, new_quantity):
        product = self.find_product(name)
        if product:
            product.quantity = new_quantity
            print(f"\nUpdated '{name}' quantity to {new_quantity}.")
        else:
            print(f"\nError: Product '{name}' not found!")

    def list_products(self):
        if not self.products:
            print("\nNo products in inventory.")
        else:
            print("\nProducts in stock:")
            for product in self.products:
                product.display_info()


def main():
    inventory = Inventory()
    while True:
        print("\n==== Inventory Manager ====")
        print("1. Add Product")
        print("2. Check Product Stock")
        print("3. Update Quantity")
        print("4. List All Products")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter product name: ").strip()
            price = float(input("Enter price: $"))
            quantity = int(input("Enter quantity: "))
            inventory.add_product(name, price, quantity)

        elif choice == "2":
            name = input("Enter product name to check: ").strip()
            product = inventory.find_product(name)
            if product:
                print("\nProduct found:")
                product.display_info()
            else:
                print(f"\nProduct '{name}' not found.")

        elif choice == "3":
            name = input("Enter product name to update: ").strip()
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_quantity(name, new_quantity)

        elif choice == "4":
            inventory.list_products()

        elif choice == "5":
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()