class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def description(self):
        return f"{self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"

    def start(self):
        return f"{self.name} is starting."

    def stop(self):
        return f"{self.name} is stopping."


class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity):
        super().__init__(name, max_speed, mileage)
        self.seating_capacity = seating_capacity

    def description(self):
        return super().description() + f", Seating Capacity: {self.seating_capacity}"

    def play_music(self, song_name):
        return f"Playing {song_name} in the {self.name}."


class Motorcycle(Vehicle):
    def __init__(self, name, max_speed, mileage, has_sidecar):
        super().__init__(name, max_speed, mileage)
        self.has_sidecar = has_sidecar

    def description(self):
        return super().description() + f", Has Sidecar: {self.has_sidecar}"

    def do_wheelie(self):
        if self.has_sidecar:
            return f"{self.name} can't perform a wheelie safely due to the sidecar."
        return f"{self.name} performs a wheelie!"
