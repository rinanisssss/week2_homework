class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Tool:
    def __init__(self):
        self.users = []

    def load_welcome_message(self, file_path):
        with open(file_path, "r") as file:
            self.welcome_message = file.read()

    def get_welcome_message(self):
        return self.welcome_message

    def show_users(self):
        for user in self.users:
            print(f"Name: {user.name} Age: {user.age}")

    def add_user(self):
        name = input("New user name > ").strip()
        age = input("New user age > ").strip()

        if not name:
            print("User name can't be blank")
            return

        if len(name) > 20:
            print("User name is too long (maximum is 20 characters)")
            return

        if not age:
            print("Age can't be blank")
            return

        if not age.isdigit() or int(age) <= 0:
            print("Age is not a positive integer")
            return

        age = int(age)

        if age > 120:
            print("Age is greater than 120")
            return

        if self.is_duplicate_user(name):
            print(f"Duplicated user name {name}")
            return

        user = User(name, age)
        self.users.append(user)
        print(f"Add new user: {name}")

    def find_user(self):
        name = input("User name > ").strip()

        found_users = [user for user in self.users if user.name == name]

        if not found_users:
            print(f"Sorry, {name} is not found")
        else:
            for user in found_users:
                print(f"Name: {user.name} Age: {user.age}")

    def delete_user(self):
        name = input("User name > ").strip()

        deleted_users = [user for user in self.users if user.name == name]

        if not deleted_users:
            print(f"Sorry, {name} is not found")
        else:
            self.users = [user for user in self.users if user.name != name]
            print(f"User {name} is deleted")

    def edit_user(self):
        name = input("User name > ").strip()

        edit_users = [user for user in self.users if user.name == name]

        if not edit_users:
            print(f"Sorry, {name} is not found")
        else:
            for user in edit_users:
                print(f"New user name({user.name}) > ", end="")
                new_name = input()
                new_name = new_name.strip() if new_name.strip() else user.name

                print(f"New user age({user.age}) > ", end="")
                new_age = input()
                new_age = new_age.strip() if new_age.strip() else str(user.age)

                if not new_age.isdigit() or int(new_age) <= 0:
                    print("Age is not a positive integer")
                    return

                new_age = int(new_age)

                if new_age > 120:
                    print("Age is greater than 120")
                    return

                user.name = new_name
                user.age = new_age
                print(f"Update user: {new_name}")

    def is_duplicate_user(self, name):
        for user in self.users:
            if user.name == name:
                return True

        return False
