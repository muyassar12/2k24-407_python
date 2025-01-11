class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def display_car_types():
        print("1 = Sedan\n2 = Hatchback\n3 = Miniwen\n4 = Suv")

    @staticmethod
    def display_models(car_type):
        model_dict = {
            "Sedan": [("BMW M5", 25000), ("Audi RS", 9000), ("Malibu", 12000)],
            "Hatchback": [("Opel Rocks", 7000), ("Toyota Corolla", 9000), ("Ford Focus", 12000)],
            "Miniwen": [("Car Max", 23000), ("Sienna Hybrid", 25000), ("Odyssey", 29000)],
            "Suv": [("Hyundai Tucson", 20000), ("Mazda CX", 15000), ("Kia Sportage", 15000)],
        }
        for i, (model, price) in enumerate(model_dict[car_type], 1):
            print(f"{i}. {model} = {price}")

    @staticmethod
    def select_type():
        while True:
            Car.display_car_types()
            car_type_choice = input("Iltimos, mashina turini tanlang: ")
            # Map the numeric input to car type names
            car_types = {
                '1': 'Sedan',
                '2': 'Hatchback',
                '3': 'Miniwen',
                '4': 'Suv'
            }
            if car_type_choice in car_types:
                return car_types[car_type_choice]
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

    @staticmethod
    def select_model(car_type):
        model_dict = {
            "Sedan": [("BMW M5", 25000), ("Audi RS", 9000), ("Malibu", 12000)],
            "Hatchback": [("Opel Rocks", 7000), ("Toyota Corolla", 9000), ("Ford Focus", 12000)],
            "Miniwen": [("Car Max", 23000), ("Sienna Hybrid", 25000), ("Odyssey", 29000)],
            "Suv": [("Hyundai Tucson", 20000), ("Mazda CX", 15000), ("Kia Sportage", 15000)],
        }
        while True:
            Car.display_models(car_type)  # Pass the actual car type name
            model_choice = input("O'zingizga kerakli bo'lgan mashina modelini tanlang (1, 2, 3): ")
            if model_choice in ['1', '2', '3']:
                model, price = model_dict[car_type][int(model_choice) - 1]
                return model, price
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

    @staticmethod
    def select_color():
        while True:
            print("1. Black (0%)\n2. White (+20%)\n3. Gray (+10%)")
            color_choice = input("Iltimos, kerakli rangni tanlang: ")
            if color_choice == "1":
                return "Black", 0
            elif color_choice == "2":
                return "White", 1.2
            elif color_choice == "3":
                return "Gray", 1.1
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

    @staticmethod
    def handle_purchase(price):
        while True:
            tolov = input(f"To'lov qilish uchun {int(price)} so'mni to'lashni xohlaysizmi? (yes/no): ").lower()
            if tolov == "yes":
                print("Xaridingiz uchun rahmat!")
                break
            elif tolov == "no":
                print("Tashrifingiz uchun rahmat!")
                break
            elif tolov == "exit":
                print("Tashrifingiz uchun rahmat! Yana kutib qolamiz.")
                break
            else:
                print("Noto'g'ri kiritingiz, qayta urinib ko'ring.")


def main():
    print("Asalomu aleykum hurmatli mijoz!")
    my_car = {"Type": "", "Model": "", "Color": "", "Price": 0}

    # Select car type
    car_type = Car.select_type()
    my_car["Type"] = car_type

    # Select car model
    model, price = Car.select_model(car_type)
    my_car["Model"] = model
    my_car["Price"] = price

    # Select car color
    color, price_multiplier = Car.select_color()
    my_car["Color"] = color
    my_car["Price"] *= price_multiplier

    # Show the selected car info
    print(f"Sizning mashinangiz {my_car['Model']} rangi: {my_car['Color']}, narxi: {int(my_car['Price'])}")

    # Handle purchase decision
    Car.handle_purchase(my_car['Price'])


if __name__ == "__main__":
    main()
