from tool import Tool

tool = Tool()
tool.load_welcome_message("welcome.txt")

while True:
    print(tool.get_welcome_message())
    command = input("Your command > ").strip().lower()

    if command == "s":
        tool.show_users()
    elif command == "a":
        tool.add_user()
    elif command == "f":
        tool.find_user()
    elif command == "d":
        tool.delete_user()
    elif command == "e":
        tool.edit_user()
    elif command == "q":
        break
    else:
        print(f"{command}: command not found")

print("Bye!")
