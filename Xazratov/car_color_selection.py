class CarColorSelection:
    def select_color(self, car):
        print(f"\n{car.model} uchun mavjud ranglar: {', '.join(car.colors)}")
        while True:
            color_choice = input("Tanlangan rangni kiriting: ").capitalize()
            if color_choice in car.colors:
                return color_choice
            else:
                print("Noto'g'ri rang. Iltimos, mavjud variantlardan birini tanlang.")
