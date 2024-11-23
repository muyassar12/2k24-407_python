class CarType:
    def __init__(self, name, available_colors):
        self.name = name
        self.available_colors = available_colors

class CarModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Car:
    def __init__(self, car_type, car_model, color):
        self.car_type = car_type
        self.car_model = car_model
        self.color = color
        self.price = car_model.price

    def display_info(self):
        print(f"Avtomobil turi: {self.car_type.name}")
        print(f"Avtomobil modeli: {self.car_model.name}")
        print(f"Rang: {self.color}")
        print(f"Narxi: {self.price}")

car_types = [
    CarType("Sedan", ["Qora", "Oq", "Kulrang"]),
    CarType("Hatchback", ["Qora", "Oq", "Kulrang"]),
    CarType("Coupe", ["Qora", "Oq", "Kulrang"]),
    CarType("Minivan", ["Qora", "Oq", "Kulrang"]),
    CarType("SUV", ["Qora", "Oq", "Kulrang"])
]

car_models = [
    CarModel("Toyota Camry", 30000),
    CarModel("Honda Civic", 32000),
    CarModel("Ford Mustang", 40000),
    CarModel("Chrysler Pacifica", 35000),
    CarModel("Toyota RAV4", 30000)
]

while True:
    print("Avtomobil turini tanlang:")
    for i, car_type in enumerate(car_types):
        print(f"{i+1}. {car_type.name}")

    try:
        car_type_choice = int(input("Tanlang: "))
        if car_type_choice < 1 or car_type_choice > len(car_types):
            print("Iltimos, 1 dan 5 gacha raqam kiriting.")
            continue
    except ValueError:
        print("Iltimos, to'g'ri raqam kiriting.")
        continue

    selected_car_type = car_types[car_type_choice - 1]

    print("Avtomobil modelini tanlang:")
    for i, car_model in enumerate(car_models):
        print(f"{i+1}. {car_model.name} - ${car_model.price}")

    try:
        car_model_choice = int(input("Tanlang: "))
        if car_model_choice < 1 or car_model_choice > len(car_models):
            print("Iltimos, 1 dan 5 gacha raqam kiriting.")
            continue
    except ValueError:
        print("Iltimos, to'g'ri raqam kiriting.")
        continue

    selected_car_model = car_models[car_model_choice - 1]

    print("Rangni tanlang:")
    for i, color in enumerate(selected_car_type.available_colors):
        print(f"{i+1}. {color}")

    try:
        color_choice = int(input("Tanlang: "))
        if color_choice < 1 or color_choice > len(selected_car_type.available_colors):
            print("Iltimos, to'g'ri rang raqamini kiriting.")
            continue
    except ValueError:
        print("Iltimos, to'g'ri raqam kiriting.")
        continue

    selected_color = selected_car_type.available_colors[color_choice - 1]

    car = Car(selected_car_type, selected_car_model, selected_color)
    car.display_info()

    confirm = input("Ushbu avtomobilni sotib olishni xohlaysizmi? (Ha/Yo'q) ")
    if confirm.lower() == "ha":
        print("Xarid amalga oshirildi.")
        break
    elif confirm.lower() == "yo'q":
        print("Xarid bekor qilindi.")
        break
    else:
        print("Iltimos, 'Ha' yoki 'Yo'q' deb javob bering.")