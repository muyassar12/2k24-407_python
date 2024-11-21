class CarModel:
    def __init__(self, model_name, base_price):
        self.model_name = model_name
        self.base_price = base_price

    def __str__(self):
        return f"{self.model_name} - ${self.base_price}"


class Color:
    def __init__(self, name, price_multiplier):
        self.name = name
        self.price_multiplier = price_multiplier

    def __str__(self):
        return f"{self.name} (Extra: {self.price_multiplier * 100}% of base price)"


class PriceAdjustment:
    def __init__(self, base_price, color):
        self.base_price = base_price
        self.color = color

    def calculate(self):
        return self.base_price * (1 + self.color.price_multiplier)


class Car:
    def __init__(self, car_type, model, color, base_price, final_price):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.base_price = base_price
        self.final_price = final_price

    def __str__(self):
        return (f"Car Type: {self.car_type}\n"
                f"Model: {self.model.model_name}\n"
                f"Color: {self.color.name}\n"
                f"Base Price: ${self.base_price}\n"
                f"Final Price (after color adjustment): ${self.final_price:.2f}")


class CarDealership:
    def __init__(self):
        self.car_types = ['Sedan', 'Hatchback', 'Coupe', 'Minivan', 'SUV']
        self.colors = [
            Color("Black", 0.02),  # 2% extra
            Color("White", 0.00),  # No extra
            Color("Gray", 0.01)  # 1% extra
        ]
        self.models = {
            'Sedan': [
                CarModel('Sedan Model A', 20000),
                CarModel('Sedan Model B', 22000),
                CarModel('Sedan Model C', 25000)
            ],
            'Hatchback': [
                CarModel('Hatchback Model A', 18000),
                CarModel('Hatchback Model B', 19500),
                CarModel('Hatchback Model C', 21000)
            ],
            'Coupe': [
                CarModel('Coupe Model A', 23000),
                CarModel('Coupe Model B', 26000)
            ],
            'Minivan': [
                CarModel('Minivan Model A', 28000),
                CarModel('Minivan Model B', 32000)
            ],
            'SUV': [
                CarModel('SUV Model A', 30000),
                CarModel('SUV Model B', 35000),
                CarModel('SUV Model C', 40000)
            ]
        }
        self.selected_car = None

    def display_menu(self, options, title):
        """Displays a list of options for the user to choose from."""
        print(title)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        return self.get_valid_input(len(options))

    def get_valid_input(self, num_choices):
        """Ensures the user enters a valid number corresponding to a menu choice."""
        while True:
            try:
                choice = int(input("Please enter your choice: "))
                if 1 <= choice <= num_choices:
                    return choice - 1  # Return zero-indexed
                else:
                    print(f"Please choose a number between 1 and {num_choices}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def select_car_type(self):
        choice = self.display_menu(self.car_types, "Please select a car type:")
        self.car_type = self.car_types[choice]
        print(f"You selected: {self.car_type}")

    def select_car_model(self):
        models = self.models[self.car_type]
        choice = self.display_menu([model.model_name for model in models], f"Select a model for {self.car_type}:")
        self.model = models[choice]
        print(f"You selected: {self.model.model_name}")

    def select_color(self):
        choice = self.display_menu([color.name for color in self.colors], "Select a color:")
        self.color = self.colors[choice]
        print(f"You selected: {self.color.name}")

    def calculate_final_price(self):
        price_adjustment = PriceAdjustment(self.model.base_price, self.color)
        return price_adjustment.calculate()

    def confirm_selection(self):
        final_price = self.calculate_final_price()
        print(f"\nPlease confirm your selection:")
        print(f"Car Type: {self.car_type}")
        print(f"Model: {self.model.model_name}")
        print(f"Color: {self.color.name}")
        print(f"Base Price: ${self.model.base_price:.2f}")
        print(f"Final Price (after color adjustment): ${final_price:.2f}")

        choice = input("Do you want to proceed with the purchase? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.selected_car = Car(self.car_type, self.model, self.color, self.model.base_price, final_price)
            print("Purchase confirmed!")
        elif choice == 'no':
            print("Purchase cancelled.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    def complete_purchase(self):
        if self.selected_car:
            print(f"\nProcessing payment...\nPayment of ${self.selected_car.final_price:.2f} completed successfully!")
            print("Thank you for your purchase.")
        else:
            print("No purchase to complete.")


def main():
    dealership = CarDealership()
    dealership.select_car_type()
    dealership.select_car_model()
    dealership.select_color()
    dealership.confirm_selection()
    dealership.complete_purchase()


if __name__ == "__main__":
    main()
