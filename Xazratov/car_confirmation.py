class CarConfirmation:
    def confirm_selection(self, car, color):
        print("\nTanlangan mashina ma'lumotlari:")
        print(f"Tur: {car.car_type}")
        print(f"Model: {car.model}")
        print(f"Rang: {color}")
        print(f"Narx: ${car.price}")
