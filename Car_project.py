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
            print("Please enter a number.")

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

print("Welcome to the Car Shop!")
print("\n1. Select a car type:")
car_types = list(set(car.car_type for car in available_cars))
display_options(car_types)
selected_type = get_user_selection(car_types, "Choose a car type: ")

print(f"\nChoose model {selected_type}:")
models = [car for car in available_cars if car.car_type == selected_type]
model_options = [car.model for car in models]
display_options(model_options)
selected_model_index = int(input("Choose a car model: ")) - 1
selected_model = models[selected_model_index]

print(f"\nChoose color {selected_model.model}:")
display_options(selected_model.colors)
selected_color = get_user_selection(selected_model.colors, "Choose a color: ")

print("\nYour choice:")
print(f"Car Type: {selected_model.car_type}")
print(f"Model: {selected_model.model}")
print(f"Color: {selected_color}")
print(f"Price: ${selected_model.price}")

confirm = input("\nDo you want to buy it? (yes/no): ").strip().lower()
if confirm == "yes":
    print("\nThank you for your purchase!")
    print(f"You bought a {selected_color} {selected_model.model} ({selected_model.car_type}) for ${selected_model.price}.")
else:
    print("\nPurchase canceled.")
1