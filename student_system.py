import json # Used for saving data nicely
import os # Used to check if file exists

# 1. OOP BASICS: creating a 'Blueprint' for a student
class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def to_dict(self):
        # Converts the object to a dictionary so we can save it
        return {"name": self.name, "roll_no": self.roll_no, "course": self.course}

# GLOBAL LIST to store all student objects
students = []
FILE_NAME = "students.json"

# 2. FILE HANDLING functions
def load_data():
    """Loads student data from the file when program starts."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                for item in data:
                    # Re-create Student objects from the loaded data
                    student = Student(item["name"], item["roll_no"], item["course"])
                    students.append(student)
            print(f"✅ Loaded {len(students)} students from file.")
        except Exception as e:
            print(f"⚠ Error loading file: {e}")

def save_data():
    """Saves the current list of students to the file."""
    try:
        with open(FILE_NAME, "w") as file:
            # Convert all student objects to dictionaries
            data_to_save = [s.to_dict() for s in students]
            json.dump(data_to_save, file, indent=4)
        print("💾 Data saved successfully!")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

# 3. CORE LOGIC functions
def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    course = input("Enter Course: ")
    # Create a new Student object
    new_student = Student(name, roll_no, course)
    students.append(new_student)
    save_data() # Auto-save after adding
    print("✅ Student added successfully!")

def view_students():
    print("\n--- Student Records ---")
    if not students:
        print("No records found.")
    else:
        print(f"{'Roll No':<10} {'Name':<20} {'Course'}")
        print("-" * 40)
        for s in students:
            print(f"{s.roll_no:<10} {s.name:<20} {s.course}")
        print("-" * 40)

# 4. MAIN LOOP (The Menu)
def main():
    load_data() # Load old data first
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
