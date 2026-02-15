# Це простий бот-асистент, який може обробляти базові команди для керування контактами
# Розбираємо вхідні дані на команду та аргументи
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Команда для додавання контакту: "add <name> <phone>"
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Команда для зміни номера контакту: "change <name> <new_phone>"
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:        
        return f"Contact '{name}' not found."


# Вивести номер зазначеного контакту: "phone <name>"
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number: {contacts[name]}"
    else:
        return f"Contact '{name}' not found."

# Вивести усі контакти
def list_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) >= 2:
                print(add_contact(args, contacts))
            else:
                print("Error: 'add' command requires name and phone number.")
        elif command == "change": 
            if len(args) >= 2:
                print(change_contact(args, contacts))
            else:
                print("Error: 'change' command requires name and new phone number.")
        elif command == "all":
            print(list_contacts(contacts))
        elif command == "phone":
            if len(args) >= 1:
                print(get_phone(args, contacts))
            else:
                print("Error: 'phone' command requires a name.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
