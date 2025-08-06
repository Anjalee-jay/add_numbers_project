def get_marks():
    while True:
        try:
            marks = float(input("Enter your marks (0 - 100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def assign_grade(marks):
    if marks >= 75:
        return 'A'
    elif marks >= 65:
        return 'B'
    elif marks >= 55:
        return 'C'
    elif marks >= 35:
        return 'S'
    else:
        return 'F'

def main():
    marks = get_marks()
    grade = assign_grade(marks)
    print(f"Your grade is: {grade}")

if __name__ == "__main__":
    main()
