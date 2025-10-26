class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Off_Road_Vehicle(Vehicle):
    def __init__(self, make, model, year, four_wheel_drive):
        super().__init__(make, model, year)
        self.four_wheel_drive = four_wheel_drive

    def display_info(self):
        super().display_info()
        print(f"Four Wheel Drive: {'Yes' if self.four_wheel_drive else 'No'}")


class Sports_Car(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Max Speed: {self.max_speed} km/h")


offroad = Off_Road_Vehicle("Jeep", "Wrangler", 2023, True)
sports_Car = Sports_Car("Ferrari", "F8 Tributo", 2022, 340)



offroad.display_info()

sports_Car.display_info()