class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}"

student = []

def main():
    while True:
        print("=== HOGWARTS MANAGEMENT SYSTEM ===")

        print("""
        1. Register Student
        2. View Student
        3. Search Student
        4. Exit
        """)

        choice = input("Choose [1, 2 etc..]: ")

        if choice == "1":
            new_student = get_student()
            student.append(new_student)
            print("Student registered successfully!")
            print(new_student)

        elif choice == "2":
            if not student:
                print("Not found")
            else:
                for index, item in enumerate(student):
                    print(
                        f"NO. {index + 1}",
                        f"Name: {item.name}",
                        f"House: {item.house}"
                    )

        elif choice == "3":
            choose = input("Search name: ")

            for item in student:
                if choose == item.name:
                    print(f"{item.name} is from {item.house}")

        elif choice == "4":
            print("Thanks")
            break

        else:
            print("Invalid!")

def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")

    return Student(name, house)

if __name__ == "__main__":
    main()
