class Car:
    def __init__(self, car_type, model, price, colors):
        self.car_type = car_type
        self.model = model
        self.price = price
        self.colors = colors

    def display_info(self):
        return f"Tur: {self.car_type}, Model: {self.model}, Narx: ${self.price}, Mavjud ranglar: {', '.join(self.colors)}"
