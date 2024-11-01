username = input("Enter a username : ")
if len(username)>12:
    print("tidak boleh lebih 12")
elif not username.find(" ") == -1:
    print("Tak boleh ada space")
else:
    print(f"welcome {username}")