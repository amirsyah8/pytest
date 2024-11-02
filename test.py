while True:
    try:
        username = input("Enter an email: ")
        if len(username) > 25:
            print("tidak boleh lebih 25")
        elif username.replace(".", "").isalnum():
            print("mus have @")
        elif username.replace("@", "").isalnum():
            print("must have .")
        else:
            print(f"Welcome {username}")
            break
    except Exception as e:
        print(f"An error occurred: {e}, please try again.")

print(f"Anda telah berjaya mencipta email {username}.")
