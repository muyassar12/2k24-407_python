

class Purchase:
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
        self.colors = {
            1: ("Black", 200),  # Black has an additional cost of $200
            2: ("White", 100),  # White has an additional cost of $100
            3: ("Gray", 300)    # Gray has an additional cost of $300
        }

    def get_car_type(self):
        print("Mashina turlari:")
        for idx, car in self.cars.items():
            print(f"{idx}. {car['type']}")
        while True:
            try:
                car_type = int(input("Moshina turini tanlang: "))
                if 1 <= car_type <= len(self.cars):
                    return car_type
                else:
                    print("Bunday turdagi avtomobil mavjud emas.")
            except ValueError:
                print("Iltimos, raqam kiriting.")

    def get_car_model(self, car_type):
        car_models = self.cars[car_type]["models"]
        print(f"{self.cars[car_type]['type']} modeli:")
        for idx, model in enumerate(car_models, 1):
            print(f"{idx}. {model['name']} - ${model['price']}")
        while True:
            try:
                model_choice = int(input("Modelni tanlang: "))
                if 1 <= model_choice <= len(car_models):
                    return car_models[model_choice - 1]
                else:
                    print("Bunday model mavjud emas.")
            except ValueError:
                print("Iltimos, raqam kiriting.")

    def get_car_color(self):
        print("Rang tanlash:")
        for idx, color in self.colors.items():
            print(f"{idx}. {color[0]} - ${color[1]}")
        while True:
            try:
                color_choice = int(input("Rangni tanlang: "))
                if 1 <= color_choice <= len(self.colors):
                    return color_choice
                else:
                    print("Bunday rang mavjud emas.")
            except ValueError:
                print("Iltimos, raqam kiriting.")

    def calculate_price(self, model, car_color_choice):
        base_price = model['price']
        color_price = self.colors[car_color_choice][1]
        total_price = base_price + color_price
        return total_price

    def purchase_car(self):
        car_type = self.get_car_type()
        model = self.get_car_model(car_type)
        car_color_choice = self.get_car_color()
        total_price = self.calculate_price(model, car_color_choice)
        print(f"\nTanlangan avtomobil: {model['name']} {self.cars[car_type]['type']} ({self.colors[car_color_choice][0]})")
        print(f"Narxi: ${total_price}")


def main():
    purchase = Purchase()
    purchase.purchase_car()

if __name__ == "__main__":
    main()
