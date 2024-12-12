class CarTypeSelection:
    def __init__(self, cars):
        self.cars = cars

    def select_type(self):
        print("Mashina turini tanlang:")
        car_types = list(set(car.car_type for car in self.cars))
        for i, car_type in enumerate(car_types, start=1):
            print(f"{i}. {car_type}")

        while True:
            try:
                type_choice = int(input("Mashina turiga mos raqamni kiriting: "))
                if type_choice >= 1 and type_choice <= len(car_types):
                    return car_types[type_choice - 1]
                else:
                    print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")
            except ValueError:
                print("Iltimos, to'g'ri raqamni kiriting.")
