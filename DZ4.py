def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact has been not found"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me all arguments"
    return wrapper

@input_error
def add_contact(args, contacts):
    if len(args) == 0:
        raise IndexError
    elif len(args) == 1:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    with open("contact_info.txt", "a") as contact_info:
        contact_info.write(f"Name: {name} \nPhone number: {phone}\n\n")
    return "Contact added."

@input_error
def change_contact(args, contacts): 
    name = args[0]
    new_phone = args[1]
    if name not in contacts:
        raise KeyError
    
    contacts[name] = new_phone
    return "Number has been changed" 
    
def database(contacts):
     with open("contact_info.txt", "a+") as contact_info:
        lines = contact_info.readlines()
        name = None
        phone = None
        for line in lines:
            line = line.strip()
            if line.startswith("Name:"):
                name = line.split(":", 1)[1].strip()
            elif line.startswith("Phone number:"):
                phone = line.split(":", 1)[1].strip()
                if name:
                    contacts[name] = phone
                    name = None
                    phone = None

@input_error
def all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        print(f"Name: {name} Phone number: {phone}")

@input_error
def user_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name not in contacts:
            raise KeyError
        return f"{name} is in base. Phone number: {contacts[name]}"
    


def main():
    contacts = {}
    database(contacts)
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            all_contacts(contacts)
        elif command == "phone":
            print(user_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
