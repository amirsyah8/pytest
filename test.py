while True:
    try:
        username = input("Enter an email: ")
        if len(username) > 12:
            print("tidak boleh lebih 12")
        elif " " in username:
            print("Tak boleh ada space")
        elif "@" not in username:
            print("Must contain @")
        else:
            print(f"Welcome {username}")
            break
    except:
        print("An error occurred, please try again.")


