class CarType:
    def __init__(self):
        self.cars = {
            1: {"type": "Sedan", "models": [
                {"name": "Toyota Camry", "price": 25000},
                {"name": "Honda Accord", "price": 26500},
                {"name": "Mazda6", "price": 27000},
                {"name": "BMW 3 Series", "price": 41500},
                {"name": "Mercedes-Benz C-Class", "price": 43000}
            ]},
            2: {"type": "Hatchback", "models": [
                {"name": "Volkswagen Golf", "price": 23500},
                {"name": "Ford Focus", "price": 22000},
                {"name": "Hyundai i30", "price": 24000},
                {"name": "Honda Civic Hatchback", "price": 25500},
                {"name": "Mazda3 Hatchback", "price": 26000}
            ]},
            3: {"type": "Coupe", "models": [
                {"name": "Ford Mustang", "price": 55000},
                {"name": "Chevrolet Camaro", "price": 50000},
                {"name": "BMW 4 Series", "price": 52000},
                {"name": "Audi A5", "price": 53500},
                {"name": "Mercedes-Benz C-Class Coupe", "price": 54000}
            ]},
            4: {"type": "Minivan", "models": [
                {"name": "Honda Odyssey", "price": 33500},
                {"name": "Toyota Sienna", "price": 34500},
                {"name": "Chrysler Pacifica", "price": 36000},
                {"name": "Kia Carnival", "price": 32500},
                {"name": "Dodge Grand Caravan", "price": 31500}
            ]},
            5: {"type": "SUV", "models": [
                {"name": "Toyota RAV4", "price": 29500},
                {"name": "Honda CR-V", "price": 28500},
                {"name": "Ford Explorer", "price": 36500},
                {"name": "Chevrolet Tahoe", "price": 49000},
                {"name": "Jeep Grand Cherokee", "price": 47500}
            ]}
        }
        self.selected_car = None

    def choose_car_type(self):
        print("Available Car Types:")
        for key, value in self.cars.items():
            print(f"{key}. {value['type']}")
        while True:
            try:
                car_type = int(input("Choose a car type: "))
                if car_type in self.cars:
                    self.selected_car = self.cars[car_type]
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        return self.selected_car


class CarModel:
    def __init__(self, selected_car):
        self.models = selected_car["models"]
        self.selected_model = None

    def choose_model(self):
        print(f"\nAvailable Models for {selected_car['type']}:")
        for idx, model in enumerate(self.models, start=1):
            print(f"{idx}. {model['name']} - ${model['price']}")
        while True:
            try:
                model_choice = int(input("Choose a model: "))
                if 1 <= model_choice <= len(self.models):
                    self.selected_model = self.models[model_choice - 1]
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        return self.selected_model


class CarColor:
    def __init__(self):
        self.colors = {
            1: ("Black", 0.2),
            2: ("White", 0.0),
            3: ("Gray", 0.1)
        }
        self.selected_color = None

    def choose_color(self):
        print("\nAvailable Colors:")
        for key, (color, price_modifier) in self.colors.items():
            print(f"{key}. {color} (Adds {price_modifier * 100}% to price)")
        while True:
            try:
                color_choice = int(input("Choose a color: "))
                if color_choice in self.colors:
                    self.selected_color = self.colors[color_choice]
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        return self.selected_color


class PriceCalculator:
    @staticmethod
    def calculate_price(selected_model, selected_color):
        base_price = selected_model["price"]
        color_modifier = selected_color[1]
        final_price = base_price + (base_price * color_modifier)
        return final_price


class Summary:
    @staticmethod
    def display(selected_car, selected_model, selected_color, final_price):
        print("\nPurchase Summary:")
        print(f"Car Type: {selected_car['type']}")
        print(f"Model: {selected_model['name']} - ${selected_model['price']}")
        print(f"Color: {selected_color[0]} (Adds {selected_color[1] * 100}% to price)")
        print(f"Final Price: ${final_price:,.2f}")



car_type_selector = CarType()
selected_car = car_type_selector.choose_car_type()

car_model_selector = CarModel(selected_car)
selected_model = car_model_selector.choose_model()

car_color_selector = CarColor()
selected_color = car_color_selector.choose_color()

final_price = PriceCalculator.calculate_price(selected_model, selected_color)
Summary.display(selected_car, selected_model, selected_color, final_price)
