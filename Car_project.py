class Car:
    def __init__(self, car_type, model, price, colors):
        self.car_type = car_type
        self.model = model
        self.price = price
        self.colors = colors

def display_options(options):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

def get_user_selection(options, prompt):
    while True:
        try:
            selection = int(input(prompt))
            if 1 <= selection <= len(options):
                return options[selection - 1]
            else:
                print("Invalid selection. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

available_cars = [
    Car("Sedan", "Toyota Camry", 25000, ["Black", "White", "Gray"]),
    Car("Sedan", "Honda Accord", 27000, ["Black", "White", "Gray"]),
    Car("Hatchback", "Ford Focus", 20000, ["Black", "Gray"]),
    Car("Hatchback", "Volkswagen Golf", 22000, ["Black", "White"]),
    Car("Coupe", "BMW 4 Series", 40000, ["White", "Gray"]),
    Car("Coupe", "Audi A5", 42000, ["Black", "White"]),
    Car("Minivan", "Honda Odyssey", 30000, ["Black", "White"]),
    Car("Minivan", "Chrysler Pacifica", 32000, ["Gray", "White"]),
    Car("SUV", "Toyota RAV4", 35000, ["Gray"]),
    Car("SUV", "Honda CR-V", 34000, ["Black", "Gray"]),
]

def main():
    try:
        print("Welcome to the Car Shop!")
        print("\n1. Select a car type:")
        car_types = sorted(list(set(car.car_type for car in available_cars)))
        display_options(car_types)
        selected_type = get_user_selection(car_types, "Choose a car type: ")

        print(f"\nChoose a model from {selected_type}:")
        models = [car for car in available_cars if car.car_type == selected_type]
        model_options = [car.model for car in models]
        display_options(model_options)
        
        while True:
            try:
                selected_model_input = input("Choose a car model by number: ")
                selected_model_index = int(selected_model_input) - 1
                if 0 <= selected_model_index < len(models):
                    selected_model = models[selected_model_index]
                    break
                else:
                    print("Invalid selection. Please choose a model number.")
            except ValueError:
                print("Please enter a number.")
        
        print(f"\nChoose a color for {selected_model.model}:")
        display_options(selected_model.colors)
        selected_color = get_user_selection(selected_model.colors, "Choose a color: ")
        
        print("\nYour choice:")
        print(f"Car Type: {selected_model.car_type}")
        print(f"Model: {selected_model.model}")
        print(f"Color: {selected_color}")
        print(f"Price: ${selected_model.price}")
        
        while True:
            confirm = input("\nDo you want to buy it? (yes/no): ").strip().lower()
            if confirm in ["yes", "y"]:
                print("\nThank you for your purchase!")
                print(f"You bought a {selected_color} {selected_model.model} ({selected_model.car_type}) for ${selected_model.price}.")
                break
            elif confirm in ["no", "n"]:
                print("\nPurchase canceled.")
                break
            else:
                print("Please enter 'yes' or 'no'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

