class CarSelectionSystem:
    def __init__(self, cars, colors, price_increase):
        self.cars = cars
        self.colors = colors
        self.price_increase = price_increase

    @staticmethod
    def choose_option(options, title):
        print(f"\n{title}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("Raqamni tanlang: ")) - 1
                if 0 <= choice < len(options):
                    return options[choice]
                else:
                    print("Noto'g'ri raqam. Qayta urinib ko'ring.")
            except ValueError:
                print("Faqat raqam kiriting!")

    def run(self):
        print("Xush kelibsiz! Avtomobil tanlash tizimi.")

        car_types = list(self.cars.keys())
        car_type = self.choose_option(car_types, "Mashina turini tanlang:")

        car_models = list(self.cars[car_type].keys())
        model = self.choose_option(car_models, f"{car_type.capitalize()} uchun modelni tanlang:")
        price = self.cars[car_type][model]


        color = self.choose_option(self.colors, "Mashina rangini tanlang:")


        if color in self.price_increase:
            price_increase_percentage = self.price_increase[color]
            price_increase_amount = (price_increase_percentage / 100) * price
            price += price_increase_amount
            print(f"\n{color.capitalize()} rangdagi mashina narxi {price_increase_percentage}% ga oshdi!")

        print("\nSiz tanlagan mashina:")
        print(f"Tur: {car_type.capitalize()}")
        print(f"Model: {model}")
        print(f"Rang: {color.capitalize()}")
        print(f"Narxi: ${price:.2f}")

        while True:
            confirm = input("Xaridni tasdiqlisizmi? (ha/yoq): ").lower()
            if confirm == "ha":
                print(f"\nTabrikliman! {color.capitalize()} rangdagi {model} {price}xarid qilindi.")
                break
            elif confirm == "yoq":
                print("\nXarid bekor qilindi. Rahmat!")
                break
            else:
                print("Siz notogri javob berdingiz. Iltimos, 'ha' yoki 'yoq' deb javob bering.")


def main():
    cars = {
        "sedan": {"Toyota Camry": 25000, "Honda Accord": 24000},
        "hatchback": {"Volkswagen Golf": 22000, "Ford Fiesta": 18000},
        "suv": {"Toyota RAV4": 27000, "Honda CR-V": 26000}
    }
    colors = ["qora", "oq", "kulrang"]
    price_increase = {
        "qora": 2,
        "oq": 5,
        "kulrang": 10
    }

    system = CarSelectionSystem(cars, colors, price_increase)
    system.run()

if __name__ == "__main__":
    main()
