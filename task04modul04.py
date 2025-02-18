from abc import ABC, abstractmethod

# Clasa abstractă Person
class Person(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self._email = email
        self._address = address
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address
    
    def check_email(self):
        return '@' in self._email
    
    @abstractmethod
    def display_info(self):
        pass

# Clasa Employee moștenește Person
class Employee(Person):
    def __init__(self, name, email, salary, address):
        super().__init__(name, email, address)
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def increase_salary(self, percentage):
        self.__salary += self.__salary * (percentage / 100)
    
    def display_info(self):
        return f"Employee: {self.name}, Email: {self._email}, Salary: {self.__salary}, Address: {self._address}"

# Clasa User moștenește Person
class User(Person):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, address)
        self.phone = phone
        self.shopping_history = []
    
    def get_phone(self):
        return self.phone
    
    def set_phone(self, phone):
        self.phone = phone
    
    def add_product(self, product):
        self.shopping_history.append(product)
    
    def total_spent(self):
        return sum(product.get_price() for product in self.shopping_history)
    
    def display_info(self):
        return f"User: {self.name}, Email: {self._email}, Phone: {self.phone}, Address: {self._address}"

# Clasa Product
class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self._description = description
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
    
    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description
    
    def check_quantity(self):
        return self.quantity >= 10

# main.py
products = [
    Product("Laptop", 3500.99, 15, "Laptop performant"),
    Product("Mouse", 150.50, 5, "Mouse wireless"),
    Product("Tastatura", 200.00, 25, "Tastatura mecanica"),
    Product("Monitor", 1200.75, 8, "Monitor Full HD"),
    Product("Casti", 300.90, 12, "Casti cu noise cancelling")
]

employees = [
    Employee("Alex Pop", "alex.pop@example.com", 4500, "Strada Libertății 12"),
    Employee("Maria Ionescu", "maria.ionescu@example.com", 5200, "Bulevardul Unirii 45")
]

users = [
    User("Ion Georgescu", "ion.geo@example.com", "0722334455", "Strada Victoriei 5"),
    User("Elena Dobre", "elena.dobre@example.com", "0744556677", "Strada Mihai Eminescu 10"),
    User("Radu Dumitru", "radu.d@example.com", "0733667788", "Bulevardul Carol 25")
]

users[0].add_product(products[0])
users[0].add_product(products[1])

print("\nInformatii utilizatori:")
for user in users:
    print(user.display_info())
    print(f"Total cheltuit: {user.total_spent()} RON")

print("\nInformatii angajati:")
for employee in employees:
    print(employee.display_info())
