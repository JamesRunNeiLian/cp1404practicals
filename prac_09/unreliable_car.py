import random

from prac_06.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that include reliability value."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only drive when random number is less than the car's reliability."""
        random_number = random.randint(0, 100)
        if random_number > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
