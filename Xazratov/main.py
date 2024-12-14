from car import Car
from car_type_selection import CarTypeSelection
from car_model_selection import CarModelSelection
from car_color_selection import CarColorSelection
from car_confirmation import CarConfirmation
from purchase_completion import PurchaseCompletion

def main():
    cars = [
        Car("Sedan", "Toyota Camry", 24000, ["Qora", "Oq", "Kulrang"]),
        Car("Hatchback", "Honda Fit", 16000, ["Qora", "Kulrang"]),
        Car("Coupe", "Ford Mustang", 27000, ["Oq", "Kulrang"]),
        Car("Minivan", "Chrysler Pacifica", 30000, ["Qora", "Oq"]),
        Car("SUV", "Toyota RAV4", 32000, ["Qora", "Oq", "Kulrang"]),
    ]

    car_type_selection = CarTypeSelection(cars)
    selected_type = car_type_selection.select_type()

    car_model_selection = CarModelSelection(cars)
    selected_car = car_model_selection.select_model(selected_type)

    car_color_selection = CarColorSelection()
    selected_color = car_color_selection.select_color(selected_car)

    car_confirmation = CarConfirmation()
    car_confirmation.confirm_selection(selected_car, selected_color)

    purchase_completion = PurchaseCompletion()
    purchase_completion.complete_purchase(selected_car, selected_color)


if __name__ == "__main__":
    main()
