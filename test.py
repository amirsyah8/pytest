while True:
    try:
        username = input("Enter an email: ")
        if len(username) > 25:
            print("tidak boleh lebih 25")
        elif not username.replace("@", "").replace(".", "").isalnum():
            print(f"Welcome {username}")
        else:
            print("Invalid email format.")  # Catch any other invalid formats
            break
    except Exception as e:
        print(f"An error occurred: {e}, please try again.")

print(f"Anda telah berjaya mencipta email {username}.")
