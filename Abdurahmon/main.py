# Define available car types, brands, models, and prices
car_catalog = {
    "Sedan": {
        "BMW": [("BMW 3 Series", 41000), ("BMW 5 Series", 54000)],
        "Audi": [("Audi A4", 39000), ("Audi A6", 50000)],
        "Mercedes": [("Mercedes C-Class", 42000), ("Mercedes E-Class", 54000)],
        "Tesla": [("Tesla Model 3", 45000)],
        "BYD": [("BYD Han", 30000)]
    },
    "SUV": {
        "BMW": [("BMW X5", 61000), ("BMW X3", 43000)],
        "Audi": [("Audi Q7", 55000), ("Audi Q5", 49000)],
        "Mercedes": [("Mercedes GLE", 57000), ("Mercedes GLC", 49000)],
        "Tesla": [("Tesla Model X", 89000), ("Tesla Model Y", 50000)],
        "BYD": [("BYD Tang", 32000)]
    },
    "Hatchback": {
        "BMW": [("BMW 1 Series", 35000)],
        "Audi": [("Audi A3", 33000)],
        "Mercedes": [("Mercedes A-Class", 34000)],
        "BYD": [("BYD e2", 20000)]
    },
    "Coupe": {
        "BMW": [("BMW 2 Series", 38000)],
        "Audi": [("Audi TT", 45000)],
        "Mercedes": [("Mercedes CLA", 37000)]
    },
    "Minivan": {
        "BMW": [],
        "Audi": [],
        "Mercedes": [("Mercedes V-Class", 60000)],
        "Tesla": [],
        "BYD": [("BYD Song MAX", 25000)]
    }
}

colors = ["Black", "White", "Gray"]


def display_options(options):
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    try:
        choice = int(input("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(options):
            raise ValueError("Invalid selection")
        return choice
    except ValueError as e:
        print(f"Error: {e}")
        return None


def select_car_type():
    print("Select Car Type:")
    car_types = list(car_catalog.keys())
    choice = display_options(car_types)
    if choice is None:
        return None
    return car_types[choice]


def select_car_brand(car_type):
    print(f"Select Car Brand for {car_type}:")
    car_brands = list(car_catalog[car_type].keys())
    choice = display_options(car_brands)
    if choice is None:
        return None
    return car_brands[choice]


def select_car_model(car_type, car_brand):
    print(f"Select a model from {car_brand} ({car_type}):")
    models = car_catalog[car_type][car_brand]
    if not models:
        print(f"No models available for {car_brand} in {car_type}. Please select another brand or type.")
        return None
    model_names = [model[0] for model in models]
    choice = display_options(model_names)
    if choice is None:
        return None
    return models[choice]


def select_car_color():
    print("Select Car Color:")
    choice = display_options(colors)
    if choice is None:
        return None
    return colors[choice]


def confirm_selection(car_type, car_brand, car_model, car_color):
    if not car_model:
        return False
    model_name, model_price = car_model
    print("\nConfirmation of selection:")
    print(f"Car Type: {car_type}")
    print(f"Car Brand: {car_brand}")
    print(f"Car Model: {model_name}")
    print(f"Car Color: {car_color}")
    print(f"Total Price: ${model_price}")
    confirmation = input("Do you want to proceed with the purchase? (yes/no): ")
    return confirmation.lower() == 'yes'


def main():
    try:
        car_type = select_car_type()
        if car_type is None:
            return
        car_brand = select_car_brand(car_type)
        if car_brand is None:
            return
        car_model = select_car_model(car_type, car_brand)
        if car_model is None:
            return
        car_color = select_car_color()
        if car_color is None:
            return

        if confirm_selection(car_type, car_brand, car_model, car_color):
            model_name, model_price = car_model
            print("\nPayment and completion of purchase:")
            print(
                f"Your purchase of a {car_color} {model_name} ({car_brand} - {car_type}) for ${model_price} is complete.")
        else:
            print("Purchase cancelled.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
