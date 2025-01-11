class Car:
    def __init__(self, car_type, models):
        self.car_type = car_type
        self.models = models

class CarStore:
    def __init__(self):
        self.car_categories = [
            Car("Sedan", {"Toyota Camry": 30000, "Honda Accord": 28000}),
            Car("Xetchbek", {"Ford Focus": 20000, "Volkswagen Golf": 22000}),
            Car("Kupe", {"Chevrolet Camaro": 35000, "Ford Mustang": 40000}),
            Car("Miniven", {"Honda Odyssey": 32000, "Toyota Sienna": 31000}),
            Car("SUV", {"Toyota Highlander": 40000, "Jeep Wrangler": 38000}),
        ]
        self.colors = ["Qora", "Oq", "Kulrang"]

    def display_car_types(self):
        print("\nMavjud mashina turlari:")
        for i, category in enumerate(self.car_categories, 1):
            print(f"{i}. {category.car_type}")

    def display_car_models(self, car_type_index):
        selected_category = self.car_categories[car_type_index]
        print(f"\n{selected_category.car_type} uchun mavjud modellari:")
        for i, (model, price) in enumerate(selected_category.models.items(), 1):
            print(f"{i}. {model} - ${price}")
        return selected_category

    def display_colors(self):
        print("\nMavjud ranglar:")
        for i, color in enumerate(self.colors, 1):
            print(f"{i}. {color}")

def main():
    store = CarStore()
    print("Mashina do‘koniga xush kelibsiz!")

    while True:
        store.display_car_types()
        try:
            car_type_choice = int(input("\nMashina turini tanlang (raqam kiriting): ")) - 1
            if 0 <= car_type_choice < len(store.car_categories):
                break
            else:
                print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")
        except ValueError:
            print("Noto‘g‘ri kiritish. Faqat raqam kiriting.")

    selected_category = store.display_car_models(car_type_choice)
    while True:
        try:
            model_choice = int(input("\nModelni tanlang (raqam kiriting): ")) - 1
            if 0 <= model_choice < len(selected_category.models):
                selected_model = list(selected_category.models.keys())[model_choice]
                selected_price = selected_category.models[selected_model]
                break
            else:
                print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")
        except ValueError:
            print("Noto‘g‘ri kiritish. Faqat raqam kiriting.")

    while True:
        store.display_colors()
        try:
            color_choice = int(input("\nRangni tanlang (raqam kiriting): ")) - 1
            if 0 <= color_choice < len(store.colors):
                selected_color = store.colors[color_choice]
                break
            else:
                print("Noto‘g‘ri tanlov. Qayta urinib ko‘ring.")
        except ValueError:
            print("Noto‘g‘ri kiritish. Faqat raqam kiriting.")

    print("\nSiz tanladingiz:")
    print(f"Mashina turi: {selected_category.car_type}")
    print(f"Model: {selected_model}")
    print(f"Rang: {selected_color}")
    print(f"Narxi: ${selected_price}")

    while True:
        confirm = input("\nXaridni tasdiqlaysizmi? (ha/yo‘q): ").lower()
        if confirm == "ha":
            print("\nXarid muvaffaqiyatli amalga oshirildi!")
            print(f"Umumiy narx: ${selected_price}")
            break
        elif confirm == "yo‘q":
            print("\nXarid bekor qilindi.")
            break
        else:
            print("Noto‘g‘ri kiritish. Iltimos, 'ha' yoki 'yo‘q' deb yozing.")

if __name__ == "__main__":
    main()
