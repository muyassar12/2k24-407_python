class Car:
    def __init__(self, car_type, model, price, available_colors):
        self.car_type = car_type
        self.model = model
        self.price = price
        self.available_colors = available_colors

    def display_info(self):
        return f"Type: {self.car_type}, Model: {self.model}, Price: ${self.price}"


class CarSelectionSystem:
    def __init__(self):
        self.cars = [
            Car("Sedan", "Toyota Camry", 30000, ["Black", "White", "Gray"]),
            Car("Hatchback", "Honda Civic", 25000, ["Black", "White"]),
            Car("Coupe", "Ford Mustang", 40000, ["Gray", "White"]),
            Car("Minivan", "Chrysler Pacifica", 35000, ["Black", "Gray"]),
            Car("SUV", "Jeep Wrangler", 45000, ["White", "Black"]),
        ]
        self.selected_car = None
        self.selected_color = None

    def select_car_type(self):
        print("\nAvailable car types:")
        car_types = list(set(car.car_type for car in self.cars))
        for i, car_type in enumerate(car_types, 1):
            print(f"{i}. {car_type}")
        while True:
            try:
                choice = int(input("\nSelect a car type by entering the corresponding number: "))
                if 1 <= choice <= len(car_types):
                    selected_type = car_types[choice - 1]
                    print(f"\nYou selected: {selected_type}")
                    return selected_type
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_car_model(self, car_type):
        available_models = [car for car in self.cars if car.car_type == car_type]
        print(f"\nAvailable models for {car_type}:")
        for i, car in enumerate(available_models, 1):
            print(f"{i}. {car.display_info()}")
        while True:
            try:
                choice = int(input("\nSelect a car model by entering the corresponding number: "))
                if 1 <= choice <= len(available_models):
                    self.selected_car = available_models[choice - 1]
                    print(f"\nYou selected: {self.selected_car.display_info()}")
                    return
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_car_color(self):
        print("\nAvailable colors for this model:")
        for i, color in enumerate(self.selected_car.available_colors, 1):
            print(f"{i}. {color}")
        while True:
            try:
                choice = int(input("\nSelect a color by entering the corresponding number: "))
                if 1 <= choice <= len(self.selected_car.available_colors):
                    self.selected_color = self.selected_car.available_colors[choice - 1]
                    print(f"\nYou selected: {self.selected_color}")
                    return
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def confirm_selection(self):
        print("\nYour selection:")
        print(f"Type: {self.selected_car.car_type}")
        print(f"Model: {self.selected_car.model}")
        print(f"Color: {self.selected_color}")
        print(f"Price: ${self.selected_car.price}")
        while True:
            confirmation = input("\nDo you want to confirm this purchase? (yes/no): ").lower()
            if confirmation == "yes":
                print("\nPurchase confirmed. Thank you for your purchase!")
                return True
            elif confirmation == "no":
                print("\nPurchase cancelled.")
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def run(self):
        print("Welcome to the Car Selection System!")
        car_type = self.select_car_type()
        self.select_car_model(car_type)
        self.select_car_color()
        self.confirm_selection()


if __name__ == "__main__":
    system = CarSelectionSystem()
    system.run()
