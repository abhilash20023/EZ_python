#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class SportsEquipment:
    def __init__(self, equipment_id, name, quantity, condition="Good"):
        self.equipment_id = equipment_id
        self.name = name
        self.quantity = quantity
        self.condition = condition

class Student:
    def __init__(self, usn, name, id):
        self.usn = usn
        self.name = name
        self.id = id

class EquipmentRentalSystem:
    def __init__(self):
        self.equipment_list = []
        self.students = {}

    def add_student(self, usn, name, id):
        self.students[usn] = Student(usn, name, id)
        print(f"Student {name} added successfully.")

    def add_equipment(self, equipment_id, name, quantity, condition="Good"):
        self.equipment_list.append(SportsEquipment(equipment_id, name, quantity, condition))
        print(f"{name} added to the inventory.")

    def rent_sports_equipment(self, equipment_id, usn):
        student = self.students.get(usn)
        if student:
            for equipment in self.equipment_list:
                if equipment.equipment_id == equipment_id:
                    if equipment.quantity > 0:
                        equipment.quantity -= 1
                        print(f"{equipment.name} rented successfully by {student.name}.")
                    else:
                        print("Sorry, this equipment is currently out of stock.")
                    return
            print("Equipment not found.")
        else:
            print("Student not found.")

    def track_equipment_return(self, return_id):
        for equipment in self.equipment_list:
            if equipment.equipment_id == return_id:
                equipment.quantity += 1
                equipment.condition = input("Enter the condition of the returned equipment: ")
                print(f"{equipment.name} returned successfully.")
                return
        print("Equipment not found.")

    def display_inventory(self):
        print("Current Inventory:")
        for equipment in self.equipment_list:
            print(f"ID: {equipment.equipment_id}, Name: {equipment.name}, Quantity: {equipment.quantity}, Condition: {equipment.condition}")

    def display_students(self):
        print("Registered Students:")
        for student in self.students.values():
            print(f"USN: {student.usn}, Name: {student.name}, ID: {student.id}")


# Main program
if __name__ == "__main__":
    rental_system = EquipmentRentalSystem()

    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Equipment")
        print("3. Rent Equipment")
        print("4. Return Equipment")
        print("5. Display Inventory")
        print("6. Display Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            usn = input("Enter student USN: ")
            name = input("Enter student name: ")
            id = input("Enter student ID: ")
            rental_system.add_student(usn, name, id)

        elif choice == "2":
            equipment_id = input("Enter equipment ID: ")
            name = input("Enter equipment name: ")
            quantity = int(input("Enter quantity: "))
            rental_system.add_equipment(equipment_id, name, quantity)

        elif choice == "3":
            equipment_id = input("Enter equipment ID to rent: ")
            usn = input("Enter student USN: ")
            rental_system.rent_sports_equipment(equipment_id, usn)

        elif choice == "4":
            return_id = input("Enter equipment ID to return: ")
            rental_system.track_equipment_return(return_id)

        elif choice == "5":
            rental_system.display_inventory()

        elif choice == "6":
            rental_system.display_students()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


# In[ ]:




