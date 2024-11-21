class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def select_type(self, my_car):
        while True:
            turi = input("Iltimos, mashina turini tanlang:\n1 = Sedan\n2 = Hatchback\n3 = Miniwen\n4 = Suv\n")
            if turi == '1':
                my_car["Type"] = "Sedan"
                print(f"1. BMW M5 = 25000\n2. Audi RS = 9000\n3. Malibu = 12000")
                break
            elif turi == '2':
                my_car["Type"] = "Hatchback"
                print(f"1. Opel Rocks = 7000\n2. Toyota Corolla = 9000\n3. Ford Focus = 12000")
                break
            elif turi == '3':
                my_car["Type"] = "Miniwen"
                print(f"1. Car Max = 23000\n2. Sienna Hybrid = 25000\n3. Odyssey = 29000")
                break
            elif turi == '4':
                my_car["Type"] = "Suv"
                print(f"1. Hyundai Tucson = 20000\n2. Mazda CX = 15000\n3. Kia Sportage = 15000")
                break
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

    def select_model(self, my_car):
        model_dict = {
            "Sedan": [("BMW M5", 25000), ("Audi RS", 9000), ("Malibu", 12000)],
            "Hatchback": [("Opel Rocks", 7000), ("Toyota Corolla", 9000), ("Ford Focus", 12000)],
            "Miniwen": [("Car Max", 23000), ("Sienna Hybrid", 25000), ("Odyssey", 29000)],
            "Suv": [("Hyundai Tucson", 20000), ("Mazda CX", 15000), ("Kia Sportage", 15000)],
        }
        while True:
            model = input("O'zingizga kerakli bo'lgan mashina modelini tanlang (1, 2, 3): ")
            if model in ["1", "2", "3"]:
                index = int(model) - 1
                car = model_dict[my_car["Type"]][index]
                my_car["Model"] = car[0]
                my_car["Price"] = car[1]
                print(f"Sizning mashinangiz {car[0]} narxi: {car[1]}")
                break
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

    def select_color(self, my_car):
        print("1. Black (0%)\n2. White (+20%)\n3. Gray (+10%)")
        while True:
            color = input("Iltimos, kerakli rangni tanlang: ")
            if color == "1":
                my_car["Color"] = "Black"
                break
            elif color == "2":
                my_car["Color"] = "White"
                my_car["Price"] *= 1.2
                break
            elif color == "3":
                my_car["Color"] = "Gray"
                my_car["Price"] *= 1.1
                break
            else:
                print("Noto'g'ri tanlov. Qayta urinib ko'ring.")
        print(f"Sizning mashinangiz {my_car['Model']}, rangi: {my_car['Color']}, narxi: {int(my_car['Price'])}")


def main():
    my_car = {"Type": "", "Model": "", "Color": "", "Price": 0}
    print("Asalomu aleykum hurmatli mijoz!")
    car = Car("", 0)
    car.select_type(my_car)
    car.select_model(my_car)
    car.select_color(my_car)

    buy = input("Mashina sotib olishni xohlaysizmi? (yes/no): ").lower()
    if buy == "yes":
        print(f"Iltimos, to'lov qiling. Sizdan {int(my_car['Price'])} talab qilinadi.")
        while True:
            tolov = input("To'lov qilish uchun 1 ni bosing yoki 'exit' deb yozing: ")
            if tolov == "1":
                print("Xaridingiz uchun rahmat!")
                break
            elif tolov == "exit":
                print("Tashrifingiz uchun rahmat!")
                break
            else:
                print("Noto'g'ri kiritingiz, qayta urinib ko'ring.")
    else:
        print("Tashrifingiz uchun rahmat! Yana kutib qolamiz.")


if __name__ == "__main__":
    main()
