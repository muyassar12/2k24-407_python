class CarData:
    def __init__(self, car_types, car_models, colors):
        self.car_types = car_types
        self.car_models = car_models
        self.colors = colors

    def get_car_models(self, selected_type):
        return self.car_models.get(selected_type, [])

class CarSelection:
    def __init__(self, car_data):
        self.car_data = car_data
        self.selected_type = None
        self.selected_model = None
        self.selected_price = None
        self.selected_color = None

    def choose_car_type(self):
        print("Mavjud mashina turlari:")
        for i, car in enumerate(self.car_data.car_types, 1):
            print(f"{i}. {car}")
        choice = int(input("Mashina turini tanlash uchun raqamni kiriting: "))
        self.selected_type = self.car_data.car_types[choice - 1]
        print(f"Siz tanladingiz: {self.selected_type}")

    def choose_car_model(self):
        models = self.car_data.get_car_models(self.selected_type)
        print("\nMavjud modellar:")
        for i, (model, price) in enumerate(models, 1):
            print(f"{i}. {model} - ${price}")
        choice = int(input("Modelni tanlash uchun raqamni kiriting: "))
        self.selected_model, self.selected_price = models[choice - 1]
        print(f"Siz tanladingiz: {self.selected_model} - ${self.selected_price}")

    def choose_color(self):
        print("\nMavjud ranglar:")
        for i, color in enumerate(self.car_data.colors, 1):
            print(f"{i}. {color}")
        choice = int(input("Rangni tanlash uchun raqamni kiriting: "))
        self.selected_color = self.car_data.colors[choice - 1]
        print(f"Siz tanladingiz: {self.selected_color}")

    def confirm_purchase(self):
        print("\nSizning tanlovingiz:")
        print(f"Mashina turi: {self.selected_type}")
        print(f"Model: {self.selected_model}")
        print(f"Rang: {self.selected_color}")
        print(f"Narxi: ${self.selected_price}")
        confirm = input("Xaridni tasdiqlaysizmi? (ha/yo'q): ")
        if confirm.lower() == "ha":
            print("Xarid muvaffaqiyatli yakunlandi!")
            print(f"Umumiy narx: ${self.selected_price}")
        else:
            print("Xarid bekor qilindi.")



if __name__ == "__main__":
    car_types = ["Sedan", "Hatchback", "Coupe", "Minivan", "SUV"]
    car_models = {
        "Sedan": [("Model S", 30000), ("Model E", 25000)],
        "Hatchback": [("Model H1", 20000), ("Model H2", 22000)],
        "Coupe": [("Coupe A", 35000), ("Coupe B", 37000)],
        "Minivan": [("Van X", 28000), ("Van Y", 29000)],
        "SUV": [("SUV Z", 40000), ("SUV T", 42000)],
    }
    colors = ["Qora", "Oq", "Kulrang"]

    car_data = CarData(car_types, car_models, colors)
    car_selector = CarSelection(car_data)
    car_selector.choose_car_type()
    car_selector.choose_car_model()
    car_selector.choose_color()
    car_selector.confirm_purchase()
