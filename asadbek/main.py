class Car:
    TAX_RATE = 0.1

    def __init__(self, car_type, model, color, price):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.price = price

    def calculate_total_price(self):
        return self.price * (1 + self.TAX_RATE)

    def display_info(self):
        info = [
            f"\nSelected Car Information:",
            f"Type: {self.car_type}",
            f"Model: {self.model}",
            f"Color: {self.color}",
            f"Base Price: ${self.price:.2f}",
            f"Total Price (with tax): ${self.calculate_total_price():.2f}"
        ]
        print("\n".join(info))


def display_menu():
    menu = [
        "\nWelcome to the Car Purchase System!",
        "Please select a car type:",
        "1. Sedan",
        "2. Hatchback",
        "3. Coupe",
        "4. Minivan",
        "5. SUV",
        "0. Exit"
    ]
    print("\n".join(menu))


def get_choice(options, prompt="Enter your choice: "):
    while True:
        try:
            choice = int(input(prompt))
            if 0 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def select_car_type():
    display_menu()
    car_types = {
        1: ("Sedan", [("Model A", 25000), ("Model B", 28000)]),
        2: ("Hatchback", [("Model C", 20000), ("Model D", 22000)]),
        3: ("Coupe", [("Model E", 30000), ("Model F", 35000)]),
        4: ("Minivan", [("Model G", 35000), ("Model H", 37000)]),
        5: ("SUV", [("Model I", 40000), ("Model J", 45000)])
    }
    choice = get_choice(car_types, "Enter the number for your choice: ")
    if choice == 0:
        print("Exiting the system.")
        return None, None, None
    car_type, models = car_types[choice]
    colors = ["Black", "White", "Gray"]
    return car_type, models, colors


def select_car_model(models):
    print("\nAvailable models:")
    for idx, (model, price) in enumerate(models, start=1):
        print(f"{idx}. {model} - ${price}")
    choice = get_choice(models, "Enter the number for your choice: ")
    return models[choice - 1]


def select_car_color(colors):
    print("\nAvailable colors:")
    for idx, color in enumerate(colors, start=1):
        print(f"{idx}. {color}")
    choice = get_choice(colors, "Enter the number for your choice: ")
    return colors[choice - 1]


def main():
    while True:
        car_type, models, colors = select_car_type()
        if car_type is None:
            break

        model_name, model_price = select_car_model(models)
        color_name = select_car_color(colors)

        car = Car(car_type, model_name, color_name, model_price)
        car.display_info()

        confirm = input("\nDo you want to confirm the purchase? (yes/no): ").strip().lower()
        if confirm == "yes":
            print(f"\nFinal Price: ${car.calculate_total_price():.2f}")
            print("Purchase complete. Thank you for your order!")
            break
        else:
            print("Purchase cancelled. Returning to main menu.")


if __name__ == "__main__":
    main()
