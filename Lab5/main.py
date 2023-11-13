import math
from datetime import date


# 1. Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods
# to calculate area and perimeter for each shape.

class Shape:
    def __init__(self, coord_x_of_center, coord_y_of_center):
        self.center_coord = (coord_x_of_center, coord_y_of_center)


class Circle(Shape):
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Circle radius must be a positive number")

        super().__init__(x, y)
        self.no_of_edges = 0
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        if height < 0:
            raise ValueError("Rectangle height must be a positive number")
        if width < 0:
            raise ValueError("Rectangle width must be a positive number")

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
    def __init__(self, x, y, side_a, side_b, side_c):
        super().__init__(x, y)
        self.no_of_edges = 3
        self.sides = [side_a, side_b, side_c]

        if side_a < 0 or side_b < 0 or side_c < 0:
            raise ValueError("Triangle edge lengths must be positive numbers")

        if side_a > side_b + side_c or side_b > side_a + side_c or side_c > side_a + side_b:
            raise ValueError("Invalid edge lengths provided")

    def area(self):
        s = self.perimeter() / 2
        return ((s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]) * s) ** (1 / 2)

    def perimeter(self):
        return self.sides[0] + self.sides[1] + self.sides[2]

    def is_right_triangle(self):
        longest_edge = max(self.sides)
        s = 0
        for edge in self.sides:
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
    INTEREST_RATE = 0.04

    def __init__(self, owner, date_of_creation):
        super().__init__(owner, date_of_creation)
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
        return self.balance * SavingsAccount.INTEREST_RATE


# Create a base class Vehicle with attributes like make, model, and year, and
# then create subclasses for specific types of vehicles like Car, Motorcycle,
# and Truck. Add methods to calculate mileage or towing capacity based on the
# vehicle type.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_used, km_travelled):
        super().__init__(make, model, year)
        self.no_of_wheels = 4
        self.permit_needed = 'B'
        self.fuel_used = fuel_used
        self.km_travelled = km_travelled

    def calculate_mileage(self):
        return self.km_travelled / self.fuel_used


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_used, km_travelled):
        super().__init__(make, model, year)
        self.no_of_wheels = 2
        self.permit_needed = 'A'
        self.fuel_used = fuel_used
        self.km_travelled = km_travelled

    def calculate_mileage(self):
        return self.km_travelled / self.fuel_used


class Truck(Vehicle):
    def __init__(self, towing_capacity, make, model, year):
        super().__init__(make, model, year)
        self.no_of_wheels = 18
        self.permit_needed = 'C'
        self.weight_attached = 0
        self.towing_capacity = towing_capacity

    def add_weight(self, weight_to_add):
        if self.weight_attached + weight_to_add > self.towing_capacity:
            raise Exception("Towing capacity exceeded")
        else:
            self.weight_attached += weight_to_add

    def remove_weight(self, weight_to_remove):
        if self.weight_attached - weight_to_remove < 0:
            raise Exception("Weight attached cannot be less than 0")
        else:
            self.weight_attached -= weight_to_remove


# 4. Build an employee hierarchy with a base class Employee. Create subclasses for
# different types of employees like Manager, Engineer, and Salesperson. Each
# subclass should have attributes like salary and methods related to their roles.

class Employee:
    def __init__(self, name, date_of_employment):
        self.name = name
        self.date_of_employment = date_of_employment

    def is_eligible_for_promotion(self):
        return (date.today() - self.date_of_employment).days > 365


class Manager(Employee):
    def __init__(self, name, date_of_employment):
        super().__init__(name, date_of_employment)
        self.employees_managed = []

    def add_employee(self, employee: Employee):
        self.employees_managed.append(employee)

    def remove_employee(self, employee: Employee):
        try:
            self.employees_managed.remove(employee)
        except ValueError:
            raise ValueError(f"Employee {employee.name} is not currently managed by manager {self.name}")


class Engineer(Employee):
    def __init__(self, name, date_of_employment, manager: Manager, project):
        super().__init__(name, date_of_employment)
        self.manager = manager
        self.project = project

    def change_manager(self, new_manager):
        self.manager = new_manager

    def change_project(self, new_project):
        self.project = new_project


class Salesperson(Employee):
    def __init__(self, name, date_of_employment, manager: Manager):
        super().__init__(name, date_of_employment)
        self.manager = manager
        self.products_sold = []

    def change_manager(self, new_manager):
        self.manager = new_manager

    def add_product_sold(self, product):
        self.products_sold.append(product)

    def remove_product_sold(self, product):
        try:
            self.products_sold.remove(product)
        except ValueError:
            raise ValueError(f"Product {product} is not currently sold by salesperson {self.name}")


# 5. Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish. Add properties and methods
# to represent characteristics unique to each animal group.

class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)

    def give_birth(self):
        print(f"Mammal {self.name} gives birth")

    def run(self):
        print(f"Mammal {self.name} runs")


class Bird(Animal):
    def __init__(self, name, habitat, wing_span):
        super().__init__(name, habitat)
        self.wing_span = wing_span

    def lay_eggs(self):
        print(f"Bird {self.name} lays eggs")

    def fly(self):
        print(f"Bird {self.name} flies")


class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def lay_eggs(self):
        print(f"Fish {self.name} lays eggs")

    def swim(self):
        print(f"{self.name} is swimming")


# 6. Design a library catalog system with a base class LibraryItem and subclasses
# for different types of items like Book, DVD, and Magazine. Include methods to
# check out, return, and display information about each item.

class LibraryItem:
    def __init__(self):
        self.checked_out = False
        self.checked_out_date = None
        self.name_of_borrower = None

    def check_out(self, name_of_borrower):
        if self.checked_out:
            raise Exception("Item is already checked out")
        else:
            self.name_of_borrower = name_of_borrower
            self.checked_out_date = date.today()
            self.checked_out = True

    def return_item(self):
        if not self.checked_out:
            raise Exception("Item has not been checked out")
        else:
            self.name_of_borrower = None
            self.checked_out_date = None
            self.checked_out = False

    def display_info(self):
        if self.checked_out:
            print(f"Checked out on: {self.checked_out_date} by {self.name_of_borrower}")
        else:
            print("Available for checkout.")


class Book(LibraryItem):
    def __init__(self, title, author, year, publisher, no_of_pages):
        super().__init__()
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.no_of_pages = no_of_pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year written: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Number of pages: {self.no_of_pages}")

        super().display_info()


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__()
        self.title = title
        self.director = director
        self.duration = duration

    def display_info(self):
        print(f"Director: {self.title}")
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")
        super().display_info()


class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__()
        self.title = title
        self.issue_number = issue_number

    def display_info(self):
        print(f"Title: {self.issue_number}")
        print(f"Issue Number: {self.issue_number}")
        super().display_info()


