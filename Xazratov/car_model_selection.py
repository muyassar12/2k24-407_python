class CarModelSelection:
    def __init__(self, cars):
        self.cars = cars

    def select_model(self, car_type):
        available_models = [car for car in self.cars if car.car_type == car_type]
        print(f"\n{car_type} uchun mavjud modellari:")
        for i, car in enumerate(available_models, start=1):
            print(f"{i}. {car.model} - ${car.price}")

        while True:
            try:
                model_choice = int(input("Modelga mos raqamni kiriting: "))
                if model_choice >= 1 and model_choice <= len(available_models):
                    return available_models[model_choice - 1]
                else:
                    print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")
            except ValueError:
                print("Iltimos, to'g'ri raqamni kiriting.")
