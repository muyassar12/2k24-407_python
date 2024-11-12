class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Sedan(Car):
    pass


class Hatchback(Car):
    pass


class Miniwen(Car):
    pass

class Suv(Car):
    pass


def select_type(my_car):
    while True:
        turi = input("Iltimos, mashina turini tanlang:\n1 = Sedan\n2 = Hatchback\n3 = Miniwen\n4 = Suv\n")
        if turi == 'Sedan' or turi == '1':
            my_car["Type"] = "Sedan"
            print(f"Bizda mavjud bo'lgan mashinalar \n1.{bmw_m5.name}={bmw_m5.price} \n2.{audi_rs.name}={audi_rs.price} \n3.{malibu.name}={malibu.price}\n")
            break
        elif turi == 'Hatchback' or turi == '2':
            my_car["Type"] = "Hatchback"
            print(f"Bizda mavjud bo'lgan mashina turlari \n1.{opel_rocks.name}={opel_rocks.price}\n2.{toyota_corolla.name}={toyota_corolla.price} \n3.{ford_focus.name}={ford_focus.price}\n")
            break
        elif turi == 'Miniwen' or turi == '3':
            my_car["Type"] = "Miniwen"
            print(f"Bizda mavjud bo'lgan mashina turlari \n1.{car_max.name}={car_max.price}  \n2.{sienna_hybrid.name}={sienna_hybrid.price} \n3.{odyssey.name}={odyssey.price}\n")
            break
        elif turi == 'Suv' or turi == '4':
            my_car["Type"] = "Suv"
            print(f"Bizda mavjud bo'lgan mashina turlari \n1.{hyundai_tucson.name}={hyundai_tucson.price}  \n2.{mazda_cx.name}={mazda_cx.price} \n3.{kia_sportage.name}={kia_sportage.price}\n")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

def select_model(my_car):
    while True:
        model = input("O'zingizga kerakli bo'lgan mashina modelini tanlang: ")
        if my_car["Type"] == "Sedan":
            if model == "1":
                my_car["Model"] = bmw_m5.name
                my_car["Price"] = bmw_m5.price
                print(f"Sizning mashinangiz {bmw_m5.name}")
                break
            elif model == "2":
                my_car["Model"] = audi_rs.name
                my_car["Price"] = audi_rs.price
                print(f"Sizning mashinangiz {audi_rs.name}")
                break
            elif model == "3":
                my_car["Model"] = malibu.name
                my_car["Price"] = malibu.price
                print(f"Sizning mashinangiz {malibu.name}")
                break
        elif my_car["Type"] == "Hatchback":
            if model == "1":
                my_car["Model"] = opel_rocks.name
                my_car["Price"] = opel_rocks.price
                print(f"Sizning mashinangiz {opel_rocks.name}")
                break
            elif model == "2":
                my_car["Model"] = toyota_corolla.name
                my_car["Price"] = toyota_corolla.price
                print(f"Sizning mashinangiz {toyota_corolla.name}")
                break
            elif model == "3":
                my_car["Model"] = ford_focus.name
                my_car["Price"] = ford_focus.price
                print(f"Sizning mashinangiz {ford_focus.name}")
                break
        elif my_car["Type"] == "Miniwen":
            if model == "1":
                my_car["Model"] = car_max.name
                my_car["Price"] = car_max.price
                print(f"Sizning mashinangiz {car_max.name}")
                break
            elif model == "2":
                my_car["Model"] = sienna_hybrid.name
                my_car["Price"] = sienna_hybrid.price
                print(f"Sizning mashinangiz {sienna_hybrid.name}")
                break
            elif model == "3":
                my_car["Model"] = odyssey.name
                my_car["Price"] = odyssey.price
                print(f"Sizning mashinangiz {odyssey.name}")
                break
        elif my_car["Type"] == "Suv":
            if model == "1":
                my_car["Model"] = hyundai_tucson.name
                my_car["Price"] = hyundai_tucson.price
                print(f"Sizning mashinangiz {hyundai_tucson.name}")
                break
            elif model == "2":
                my_car["Model"] = mazda_cx.name
                my_car["Price"] = mazda_cx.price
                print(f"Sizning mashinangiz {mazda_cx.name}")
                break
            elif model == "3":
                my_car["Model"] = kia_sportage.name
                my_car["Price"] = kia_sportage.price
                print(f"Sizning mashinangiz {kia_sportage.name}")
                break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")

def select_color(my_car):
    color1()
    while True:
        color = input("Iltimos, kerakli rangni tanlang: ")
        if color.lower() == "black" or color == "1":
            my_car["Color"] = "Black"
            break
        elif color.lower() == "white" or color == "2":
            my_car["Color"] = "White"
            my_car["Price"] *= 1.20
            break
        elif color.lower() == "gray" or color == "3":
            my_car["Color"] = "Gray"
            my_car["Price"] *= 1.10
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")
    print(f"Sizning mashinangiz {my_car['Model']}, rangi: {my_car['Color']}, narxi: {int(my_car['Price'])}")

def color1():
    print("Black + 0%")
    print("White + 20%")
    print("Gray + 10%")


my_car = {"Type": "", "Model": "", "Color": "", "Price": 0}

# Mashina obyektlari yaratish
bmw_m5 = Sedan("BMW M5", 25000)
audi_rs = Sedan("Audi RS", 9000)
malibu = Sedan("Malibu", 12000)

opel_rocks = Hatchback("Opel Rocks", 7000)
toyota_corolla = Hatchback("Toyota Corolla", 9000)
ford_focus = Hatchback("Ford Focus", 12000)

car_max = Miniwen("Car Max", 23000)
sienna_hybrid = Miniwen("Sienna Hybrid", 25000)
odyssey = Miniwen("Odyssey", 29000)

hyundai_tucson = Suv("Hyundai Tucson", 20000)
mazda_cx = Suv("Mazda CX", 15000)
kia_sportage = Suv("Kia Sportage", 15000)

started = input("Asalomu aleykum hurmatli mijoz, ismingizni bilsam bo'ladimi? ")
print(f"{started}, sizga qaysi mashina turi kerak?")

select_type(my_car)
select_model(my_car)
select_color(my_car)

buy = input("Mashina sotib olishni xohlaysizmi? (yes/no): ")
if buy.lower() == "yes":
    print(f"Iltimos, to'lov qiling. Sizdan {int(my_car['Price'])}  talab qilinadi.")
    while True:
        tolov = input("To'lov qilish uchun 1 ni bosing: ")
        if tolov == "1":
            print("Xaridingiz uchun rahmat!")
            break
        else:
            print("Noto'g'ri kiritingiz, qayta urinib ko'ring.")

else:
    print("Tashrifingiz uchun rahmat! Sizni xarid qilishingiz uchun yana kutib qolamiz")













