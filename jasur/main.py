class Avtosalon:
    def __init__(self):
        self.cars = {
            "Sedan": {"Toyota Camry": 30000, "Honda Accord": 28000},
            "Hatchback": {"Ford Fiesta": 15000, "Volkswagen Golf": 20000},
            "Coupe": {"Chevrolet Camaro": 35000, "Ford Mustang": 40000},
            "Minivan": {"Honda Odyssey": 33000, "Toyota Sienna": 35000},
            "SUV": {"Toyota RAV4": 27000, "Honda CR-V": 26000}
        }
        self.colors = ["black", "white", "gray"]
        self.color_prices = {"black": 500, "white": 300, "gray": 0}

    def start(self):
        while True:
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ")
            print("♦️  ⚠️  Cars option:                ♦️")
            print("♦️  1️⃣  Sedan                       ♦️")
            print("♦️  2️⃣  Hatchback                   ♦️")
            print("♦️  3️⃣  Coupe                       ♦️")
            print("♦️  4️⃣  Minivan                     ♦️")
            print("♦️  5️⃣  SUV                         ♦️")
            print("♦️  6️⃣  Exit                        ♦️")
            print("♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ♦️ ")

            option = input("Choose option (1-6):\n>>> ")
            if option == "6":
                self.exit()
                exit()
            elif option in ["1", "2", "3", "4", "5"]:
                car_type = list(self.cars.keys())[int(option) - 1]
                self.select_car_type(car_type)
            else:
                print("Invalid option. Please choose a number between 1 and 6.")

    def select_car_type(self, car_type):
        print(f"\nAvailable car models for {car_type}:")
        models = self.cars[car_type]
        for i, model in enumerate(models, start=1):
            print(f"{i}. {model} - ${models[model]}")

        model_choice = input(f"Choose a model (1-{len(models)}):\n>>> ")
        if model_choice.isdigit() and 1 <= int(model_choice) <= len(models):
            selected_model = list(models.keys())[int(model_choice) - 1]
            price = models[selected_model]
            self.select_color(car_type, selected_model, price)
        else:
            print("Invalid choice. Please enter a valid model number.")

    def select_color(self, car_type, model, price):
        print("\nAvailable colors:")
        for i, color in enumerate(self.colors, start=1):
            print(f"{i}. {color} (+${self.color_prices[color]})")

        color_choice = input(f"Choose a color (1-{len(self.colors)}):\n>>> ")
        if color_choice.isdigit() and 1 <= int(color_choice) <= len(self.colors):
            selected_color = self.colors[int(color_choice) - 1]
            color_price = self.color_prices[selected_color]
            final_price = price + color_price
            self.confirm_selection(car_type, model, selected_color, final_price)
        else:
            print("Invalid color choice. Please enter a valid color number.")

    def confirm_selection(self, car_type, model, color, price):
        print("\nSelected Car Details:")
        print(f"Type: {car_type}")
        print(f"Model: {model}")
        print(f"Color: {color}")
        print(f"Price: ${price}")

        confirmation = input("Confirm purchase? (1.yes/2.no)\n>>> ")
        if confirmation == "1":
            self.complete_purchase(price)
        elif confirmation == "2":
            print("Purchase cancelled.")
        else:
            print("Invalid input. Please enter '1' or '2'.")

    def complete_purchase(self, price):
        print(f"\nThank you for your purchase! The total price is ${price}.")
        print("Purchase completed successfully.\n")

        continue_option = input("Would you like to buy another car or exit? (1.buy again/2.exit)\n>>> ")
        if continue_option == "1":
            self.start()
        elif continue_option == "2":
            self.exit()
            exit()
        else:
            print("Invalid input. Please enter '1' to buy again or '2' to exit.")

    def exit(self):
        print("Thank you for visiting our Avtosalon. Goodbye!")

if __name__ == "__main__":
    avtosalon = Avtosalon()
    avtosalon.start()
