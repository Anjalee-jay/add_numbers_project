from inputs import get_numbers
from calculator import add

def main():
    while True:
        num1, num2 = get_numbers()
        result = add(num1, num2)
        print(f"Result: {result}")

        again = input("Do you want to add more numbers? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exit")
            break

if __name__ == "__main__":
    main()
