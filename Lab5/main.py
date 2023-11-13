import math
from enum import Enum


# Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods
# to calculate area and perimeter for each shape.

class Shape:
    def __init__(self, coord_x_of_center, coord_y_of_center):
        self.center_coord = (coord_x_of_center, coord_y_of_center)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)

        self.no_of_edges = 0
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.no_of_edges = 4
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def length_of_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** (1 / 2)


class Triangle(Shape):
    def __init__(self, x, y, len_a, len_b, len_c):
        super().__init__(x, y)
        self.no_of_edges = 3
        self.edges = [len_a, len_b, len_c]

    def area(self):
        s = self.perimeter() / 2
        return ((s - self.edges[0]) * (s - self.edges[1]) * (s - self.edges[2]) * s) ** (1 / 2)

    def perimeter(self):
        return self.edges[0] + self.edges[1] + self.edges[2]

    def is_right_triangle(self):
        longest_edge = max(self.edges)
        s = 0
        for edge in self.edges:
            if edge != longest_edge:
                s += edge ** 2
        return longest_edge ** 2 == s


# Design a bank account system with a base class Account and subclasses SavingsAccount
# and CheckingAccount. Implement methods for deposit, withdrawal, and interest
# calculation.


class Account:
    def __init__(self, owner, date_of_creation):
        self.owner = owner
        self.date_of_creation = date_of_creation
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount


class CheckingAccount(Account):
    def __init__(self, owner, date_of_creation):
        super().__init__(owner, date_of_creation)

    def withdrawal(self, amount):
        if self.balance < amount:
            raise Exception("Not enough money in account")
        else:
            self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, owner, date_of_creation):
        super().__init__(owner, date_of_creation)
        self.interest = 0.04
        self.withdrawals_per_month = 6

    def withdrawal(self, amount):
        if self.balance < amount:
            raise Exception("Not enough money in account")
        elif self.withdrawals_per_month == 0:
            raise Exception("The limit for withdrawals has been reached for this month")
        else:
            self.balance -= amount
            self.withdrawals_per_month -= 1

    def compute_interest(self):
        return self.balance * self.interest


# Create a base class Vehicle with attributes like make, model, and year, and
# then create subclasses for specific types of vehicles like Car, Motorcycle,
# and Truck. Add methods to calculate mileage or towing capacity based on the
# vehicle type.
class Location(Enum):
    IN_TRAFFIC = 1
    IN_CITY = 2
    OUTSIDE_CITY = 3


class VehicleSpecifications:
    def __init__(self, make, model, year, fuel_tank_capacity,
                 mileage_in_traffic, mileage_in_city, mileage_outside_city,
                 towing_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_tank_capacity = fuel_tank_capacity
        self.mileage = {Location.IN_TRAFFIC: mileage_in_traffic,
                        Location.IN_CITY: mileage_in_city,
                        Location.OUTSIDE_CITY: mileage_outside_city}
        self.towing_capacity = towing_capacity


class Vehicle:
    def __init__(self, vehicle_specs: VehicleSpecifications):
        self.vehicle_specs = vehicle_specs
        self.kms_traveled_since_refuel = 0
        self.fuel = vehicle_specs.fuel_tank_capacity

    def refuel(self):
        self.fuel = self.vehicle_specs.fuel_tank_capacity
        self.kms_traveled_since_refuel = 0

    def mileage(self):
        return self.kms_traveled_since_refuel / (self.vehicle_specs.fuel_tank_capacity - self.fuel + 0.00001)

    def travel(self, kms, location: Location):
        self.kms_traveled_since_refuel += kms
        self.fuel -= self.vehicle_specs.mileage[location] * kms


class Car(Vehicle):
    def __init__(self, vehicle_specs):
        super().__init__(vehicle_specs)
        self.no_of_wheels = 4
        self.permit_needed = 'B'


class Motorcycle(Vehicle):
    def __init__(self, vehicle_specs):
        super().__init__(vehicle_specs)
        self.no_of_wheels = 2
        self.permit_needed = 'A'


class Truck(Vehicle):
    def __init__(self, vehicle_specs):
        super().__init__(vehicle_specs)
        self.no_of_wheels = 18
        self.permit_needed = 'C'
        self.weight_attached = 0

    def add_weight(self, weight_to_add):
        if self.weight_attached + weight_to_add > self.vehicle_specs.towing_capacity:
            raise Exception("Towing capacity exceeded")
        else:
            self.weight_attached += weight_to_add

    def remove_weight(self, weight_to_remove):
        if self.weight_attached - weight_to_remove < 0:
            raise Exception("Weight attached cannot be less than 0")
        else:
            self.weight_attached -= weight_to_remove


# Build an employee hierarchy with a base class Employee. Create subclasses for
# different types of employees like Manager, Engineer, and Salesperson. Each
# subclass should have attributes like salary and methods related to their roles.


