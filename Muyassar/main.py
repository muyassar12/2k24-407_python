class Car:
    def __init__(self, car_type, model, color, price):
        self.car_type = car_type
        self.model = model
        self.color = color
        self.price = price

    def display_details(self):
        print("\nSiz tanlagan mashina:")
        print(f"Mashina turi: {self.car_type}")
        print(f"Model: {self.model}")
        print(f"Rang: {self.color}")
        print(f"Narxi: ${self.price}")


def choose_option(prompt, options):
    while True:
        try:
            print(prompt)
            for i, option in enumerate(options, 1):
                if isinstance(option, tuple):
                    print(f"{i}. {option[0]} - ${option[1]}")
                else:
                    print(f"{i}. {option}")
            choice = int(input("Tanlovingizni kiriting: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Xato: 1 dan {len(options)} gacha bo'lgan raqamni tanlang.")
        except ValueError:
            print("Faqat raqam kiriting.")


def main():
    car_types = ["Sedan", "Hatchback", "Coupe", "Minivan", "SUV"]
    car_models = {
        "Sedan": [("Model S", 30000), ("Model E", 25000)],
        "Hatchback": [("Model H1", 20000), ("Model H2", 22000)],
        "Coupe": [("Coupe A", 35000), ("Coupe B", 37000)],
        "Minivan": [("Van X", 28000), ("Van Y", 29000)],
        "SUV": [("SUV Z", 40000), ("SUV T", 42000)],
    }
    colors = ["Qora", "Oq", "Kulrang"]

    selected_type = choose_option("Mavjud mashina turlari:", car_types)

    models = car_models[selected_type]
    selected_model, selected_price = choose_option("\nMavjud modellar:", models)

    selected_color = choose_option("\nMavjud ranglar:", colors)

    chosen_car = Car(selected_type, selected_model, selected_color, selected_price)

    chosen_car.display_details()
    while True:
        confirm = input("Xaridni tasdiqlaysizmi? (ha/yo'q): ").strip().lower()
        if confirm == "ha":
            print("Xarid muvaffaqiyatli yakunlandi! Rahmat!")
            break
        elif confirm == "yo'q":
            print("Xarid bekor qilindi.")
            break
        else:
            print("Noto'g'ri tanlov, iltimos 'ha' yoki 'yo'q' deb javob bering.")


if __name__ == "__main__":
    main()
