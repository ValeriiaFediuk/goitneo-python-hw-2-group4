def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact is not found."
        except IndexError:
            return "Invalid command. Please, provide both name and phone number."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command. Please, write both name and phone number."

@input_error
def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact is not found."
    else:
        return "Invalid command. Please, write both name and phone number."

@input_error
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact is not found."

@input_error      
def show_all(contacts):
    if contacts:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")
        

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
                raise ValueError("Invalid input. Please try again.")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()