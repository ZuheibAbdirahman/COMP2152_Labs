# Lab 03:Python Collections Practice
# Student Name: Zuheib Abdirahman #ID: 101549351
# Date: 2026-02-04

print("=" * 50)
print("Question 1: Student Grades List")
print("=" * 50)
# Question 1: Student Grades List
grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print("Sorted grades:", grades)
print("Highest grade:", grades[-1])  # Last element using negative indexing
print("Lowest grade:", grades[0])    # First element
print("Total number of grades:", len(grades))

print("\n" + "=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)

# Question 2: Shopping Cart
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print("Number of apples:", apple_count)

milk_position = cart.index("milk")
print("Position of milk:", milk_position)

cart.remove("apple")  # Removes first occurrence of "apple"
last_item = cart.pop()  # Removes and returns last item
print("Removed item using pop:", last_item)

has_banana = "banana" in cart
print("Is banana in cart?", has_banana)
print("Final cart:", cart)

print("\n" + "=" * 50)
print("Question 3: Coordinate System")
print("=" * 50)

# Question 3: Coordinate System
point1 = (3, 5)
point2 = (7, 2)
print("Point 1:", point1)
print("Point 2:", point2)

x1, y1 = point1  # Unpacking tuple
x2, y2 = point2  # Unpacking tuple
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")

# Calculate distance using distance formula
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between points:", distance)

# Create tuple from string
char_tuple = tuple("PYTHON")
print("Characters tuple:", char_tuple)

# Print each character
print("Characters printed individually:")
for char in char_tuple:
    print(char)

print("\n" + "=" * 50)
print("Question 4: Class Attendance")
print("=" * 50)

# Question 4: Class Attendance
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")
print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

# Set operations
both_classes = monday_class & wednesday_class  # intersection
print("Attended both classes:", both_classes)

either_class = monday_class | wednesday_class  # union
print("Attended either class:", either_class)

only_monday = monday_class - wednesday_class  # difference
print("Only Monday:", only_monday)

only_one_class = monday_class ^ wednesday_class  # symmetric difference
print("Only one class (not both):", only_one_class)
# Subset check
is_subset = monday_class <= either_class  # checks if Monday class is subset of all students
print("Is Monday subset of all students?", is_subset)

print("\n" + "=" * 50)
print("Question 5: Contact Book")
print("=" * 50)

# Question 5: Contact Book
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print("Alice's number:", contacts["Alice"])
# Add new contact
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)
# Update Bob's number
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)
# Delete Charlie
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)
# Print keys and values
print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))

print("\n" + "=" * 50)
print("Question 6: Inventory Management System")
print("=" * 50)

# Question 6: Inventory Management System
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

# Print Current Inventory
print("=== Current Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")
# Categories Set
electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
all_products = electronics | accessories  # union
print("\nAll product categories:", all_products)
# Price List
price_list = [price for price, quantity in inventory.values()]
print("\nPrice list:", price_list)
# Sort Prices
sorted_prices = sorted(price_list)
print("Sorted prices:", sorted_prices)
print("Lowest price: $" + str(sorted_prices[0]))
print("Highest price: $" + str(sorted_prices[-1]))
# Add New Product
inventory["Headphones"] = (49.99, 20)
# Update Quantity 
inventory["Mouse"] = (29.99, 12)  

# Remove Product
del inventory["Monitor"]

# Final Report
print("\n=== Final Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")

print("\n" + "=" * 50)
print("Lab Completed Successfully!")
print("=" * 50)