while True:
    try:
        number = int(input("Enter an integer: "))
        print(f"You entered: {number}")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
