class Car:
    def __init__(self, car_type, car_model, car_color, car_price):
        self.type = car_type
        self.model = car_model
        self.color = car_color
        self.price = car_price

    def confirmation(self):
        print(f"Type: {self.type}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        while True:
            confirmation1 = input("Do you wish to continue? (Y/N): ").lower()
            if confirmation1 == "y":
                print("Please wait...!")
                print("Your order has been successfully confirmed...")
                print("Thank you for your purchase!")
                break
            elif confirmation1 == "n":
                print("Your order has been canceled!")
                break
            else:
                print("Wrong input, please try again!")


def model_selection(car_type, car_models, car_prices):
    print("Choose Model of Car:")
    for i, model in enumerate(car_models, start=1):
        print(f"{i}) {model}")
    try:
        model_index = int(input("Enter your choice: ")) - 1
        if 0 <= model_index < len(car_models):
            car_model = car_models[model_index]
            car_price = car_prices[model_index]
            return car_type, car_model, car_price
        else:
            print("Invalid input. Try again.")
            return model_selection(car_type, car_models, car_prices)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return model_selection(car_type, car_models, car_prices)


def color_selection(car_type, car_model, car_price):
    colors = ["White (+3% extra)", "Black (+5% extra)", "Grey"]
    print("Available Colors:")
    for i, color in enumerate(colors, start=1):
        print(f"{i}) {color}")
    try:
        color_choice = int(input("Enter your choice: "))
        if color_choice == 1:
            car_color = "White"
            car_price += car_price * 0.03
        elif color_choice == 2:
            car_color = "Black"
            car_price += car_price * 0.05
        elif color_choice == 3:
            car_color = "Grey"
        else:
            print("Invalid Color")
            return color_selection(car_type, car_model, car_price)
        return car_type, car_model, car_color, car_price
    except ValueError:
        print("Invalid input. Please enter a number.")
        return color_selection(car_type, car_model, car_price)


def main():
    car_types = {
        "1": ("Sedan", ["BMW M5", "Tesla Model S", "Audi A6"], [145000, 95000, 60000]),
        "2": ("Hatchback", ["Volkswagen Golf R", "Toyota Prius Prime", "Mini Hardtop"], [45000, 90000, 75000]),
        "3": ("Coupe", ["Aston Martin Vantage", "BMW M2", "McLaren Artura"], [745000, 195000, 600000]),
        "4": ("Minivan", ["Mercedes-Benz Sprinter Crew Van", "Ford Transit Passenger Wagon", "Chevrolet Express Passenger"], [155000, 85000, 50000]),
        "5": ("SUV", ["Lamborghini Urus", "BMW X6M", "Aston Martin DBX"], [445000, 195000, 500000])
    }

    print("Car Types:")
    for key, (car_type, _, _) in car_types.items():
        print(f"{key}) {car_type}")

    car_choice = input("Select your car type: ")
    if car_choice in car_types:
        car_type, car_models, prices = car_types[car_choice]
        car_type, car_model, car_price = model_selection(car_type, car_models, prices)
        car_type, car_model, car_color, car_price = color_selection(car_type, car_model, car_price)
        car = Car(car_type, car_model, car_color, car_price)
        car.confirmation()
    else:
        print("Invalid Input")
        main()


if __name__ == "__main__":
    main()

