from product import Product
from employee import Employee
from user import User

# Creare produse
products = [
    Product("Laptop", 3500.0, 15, "Laptop performant pentru gaming"),
    Product("Telefon", 2500.0, 8, "Smartphone nou, 128GB"),
    Product("Căști", 300.0, 20, "Căști wireless cu noise cancelling"),
    Product("Monitor", 1200.0, 5, "Monitor 27 inch, 144Hz"),
    Product("Mouse", 150.0, 30, "Mouse ergonomic pentru gaming")
]

# Creare angajați
employees = [
    Employee("Alex Popescu", "alex@email.com", 5000.0, "Strada Libertății, nr. 10"),
    Employee("Maria Ionescu", "maria@example.com", 4800.0, "Bulevardul Victoriei, nr. 15")
]

# Creare utilizatori
users = [
    User("Andrei Radu", "andrei@email.com", "0712345678", "Strada Păcii, nr. 3"),
    User("Ioana Dumitru", "ioana@email.com", "0723456789", "Strada Unirii, nr. 12"),
    User("Mihai Georgescu", "mihai@email.com", "0734567890", "Strada Mihai Eminescu, nr. 7")
]

# Adăugare produse în istoricul de cumpărături
users[0].add_product(products[0])
users[0].add_product(products[1])
users[1].add_product(products[2])
users[2].add_product(products[3])
users[2].add_product(products[4])

# Afișare total cheltuit de fiecare utilizator
for user in users:
    print(f"{user.name} a cheltuit un total de {user.total_spent()} RON")

# Afișare informații despre utilizatori și angajați (polimorfism)
for person in users + employees:
    print(person.display_info())

# Creștere salariu pentru un angajat și afișare salariu actualizat
employees[0].increase_salary(10)
print(f"Salariul lui {employees[0].name} după mărire: {employees[0].get_salary()} RON")
