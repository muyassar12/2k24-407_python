class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.model} (${self.price})"


class CarCategory:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display_cars(self):
        print(f"\nAvailable models for {self.name}:")
        for index, car in enumerate(self.cars, start=1):
            print(f"{index}. {car}")


class CarStore:
    def __init__(self):
        self.categories = {}
        self.available_colors = ["red", "blue", "green", "silver"]

    def add_category(self, category):
        self.categories[category.name.upper()] = category

    def select_category(self):
        print("Choose a car type:")
        category_names = list(self.categories.keys())
        for index, name in enumerate(category_names, start=1):
            print(f"{index}. {name.capitalize()}")

        try:
            selection = int(input("\nEnter the number of the desired type: ")) - 1
            if 0 <= selection < len(category_names):
                return self.categories[category_names[selection]]
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            return self.select_category()

    def select_model(self, category):
        category.display_cars()
        try:
            selection = int(input("\nEnter the number of the desired model: ")) - 1
            if 0 <= selection < len(category.cars):
                return category.cars[selection]
            else:
                raise ValueError
        except ValueError:
            print("Invalid model choice. Please try again.")
            return self.select_model(category)

    def select_color(self):
        print("\nChoose a color:")
        for index, color in enumerate(self.available_colors, start=1):
            print(f"{index}. {color.capitalize()}")

        try:
            selection = int(input("\nEnter the number of the desired color: ")) - 1
            if 0 <= selection < len(self.available_colors):
                return self.available_colors[selection]
            else:
                raise ValueError
        except ValueError:
            print("Invalid color choice. Please try again.")
            return self.select_color()

    def confirm_choice(self, car, color):
        print("\nYour selection summary:")
        print(f"Model: {car.model}")
        print(f"Price: ${car.price}")
        print(f"Color: {color.capitalize()}")
        confirmation = input("\nDo you want to proceed with this purchase? (yes/no): ").lower()
        return confirmation == "yes"


def main():
    store = CarStore()

    bmw_category = CarCategory("BMW")
    bmw_category.add_car(Car("BMW 3 Series", 45000))
    bmw_category.add_car(Car("Mercedes-Benz C-Class", 47000))
    bmw_category.add_car(Car("Audi A4", 46000))

    honda_category = CarCategory("HONDA")
    honda_category.add_car(Car("Ford Focus", 22000))
    honda_category.add_car(Car("Volkswagen Polo", 21000))
    honda_category.add_car(Car("Honda Civic", 23000))

    tesla_category = CarCategory("TESLA")
    tesla_category.add_car(Car("Jeep Grand Cherokee", 45000))
    tesla_category.add_car(Car("BMW X5", 65000))
    tesla_category.add_car(Car("Tesla Model X", 70000))

    # Add categories to the store
    store.add_category(bmw_category)
    store.add_category(honda_category)
    store.add_category(tesla_category)

    print("Welcome to the car selection system!")

    category = store.select_category()
    selected_car = store.select_model(category)
    selected_color = store.select_color()

    if store.confirm_choice(selected_car, selected_color):
        print(f"\nCongratulations! You have successfully purchased a {selected_color.capitalize()} {selected_car.model}.")
        print(f"Total price: ${selected_car.price}. Thank you for your purchase!")
    else:
        print("\nThe purchase has been canceled. Thank you for visiting!")


if __name__ == "__main__":
    main()
