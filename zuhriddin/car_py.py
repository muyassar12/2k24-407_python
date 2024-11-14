class Car:
    def __init__(self):
        self.type = ""
        self.model = ""
        self.color = ""
        self.price = 0

    def confirmation(self):
        print(f"Type: {self.type}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        while True:
            confirmation1 = input("Would you like to continue? (y/n) ")
            match confirmation1:
                case "y":
                    print("Please wait...!")
                    print("Your order has been successfully confirmed...")
                    print("Thank you for your purchase!")
                    exit()
                case "n":
                    print("Your order has been canceled! ")
                    self.type = ""
                    self.model = ""
                    self.color = ""
                    self.price = 0
                    return
                case _:
                    print("Wrong input please try again!")
                    continue

    def model_selection(self, car_models, car_prices):
        model_select = input("Select model: ")
        match model_select:
            case "1":
                self.model = car_models[0]
                self.price += car_prices[0]
                self.color_selection()
            case "2":
                self.model = car_models[1]
                self.price += car_prices[1]
                self.color_selection()
            case "3":
                self.model = car_models[2]
                self.price += car_prices[2]
                self.color_selection()
            case _:
                print("Wrong Input")
                self.model_selection(car_models, car_prices)

    def color_selection(self):
        print("Available Colors: \n1)White (+3% extra)\n2)Black (+5% extra)\n3)Grey")
        color = input("Enter your choice: ")
        match color:
            case "1":
                self.color = "White"
                self.price += self.price * 0.03
                self.confirmation()
            case "2":
                self.color = "Black"
                self.price += self.price * 0.05
                self.confirmation()
            case "3":
                self.color = "Grey"
                self.confirmation()
            case _:
                print("Invalid Color")
                self.color_selection()



def main():
    car = Car()
    while True:
        print("Car Types: \n1)Sedan\n2)Hatchback\n3)Coupe\n4)Minivan\n5)SUV")
        type_select = input("Select car type: ")
        match type_select:
            case "1":
                car.type = "Sedan"
                car_models = ["BMW M5", "Tesla Model S", "Audi A6"]
                prices = [145000, 95000, 60000]
                print("Choose Model of Car: \n1)BMW M5\n2)Tesla Model S\n3)Audi A6")
                car.model_selection(car_models, prices)
            case "2":
                car.type = "Hatchback"
                car_models = ["Volkswagen Golf R", "Toyota Prius Prime", "Mini Hardtop"]
                prices = [45000, 90000, 75000]
                print("Choose Model of Car: \n1)Volkswagen Golf R\n2)Toyota Prius Prime\n3)MINI Hardtop")
                car.model_selection(car_models, prices)
            case "3":
                car.type = "Coupe"
                car_models = ["Aston Martin Vantage", "BMW M2", "McLaren Artura"]
                prices = [745000, 195000, 600000]
                print("Choose Model of Car: \n1)Aston Martin Vantage\n2)BMW M2\n3)McLaren Artura")
                car.model_selection(car_models, prices)
            case "4":
                car.type = "Minivan"
                car_models = ["Mercedes-Benz Sprinter Crew Van","Ford Transit Passenger Wagon","Chevrolet Express Passenger"]
                prices = [155000, 85000, 50000]
                print("Choose Model of Car: \n"
                      "1)Mercedes-Benz Sprinter Crew Van\n"
                      "2)Ford Transit Passenger Wagon\n"
                      "3)Chevrolet Express Passenger")
                car.model_selection(car_models, prices)
            case "5":
                car.type = "SUV"
                car_models = ["Lamborghini Urus", "BMW X6M", "Aston Martin DBX"]
                prices = [445000, 195000, 500000]
                print("Choose Model of Car: \n1)Lamborghini Urus\n2)BMW X6M\n3)Aston Martin DBX")
                car.model_selection(car_models, prices)
            case _:
                print("Invalid Input")

if __name__ == "__main__":
    main()
