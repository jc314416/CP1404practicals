from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1, 100) < self.reliability:
            distance = super().drive(distance)
        else:
            distance = 0
        return distance