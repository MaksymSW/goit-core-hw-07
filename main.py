from classes import AddressBook, Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone, please (The phone number must consist of 10 digits)"
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return "Contact added."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
    record.add_birthday(birthday)
    return 'Birthday added'


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone,new_phone)
    return "Contact updated."


@input_error
def show_phone(args, book: AddressBook):
    phone = args[0]
    record = book.find(phone)
    return '; '.join(str(phone) for phone in record.phones)

@input_error   
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return record.birthday

@input_error
def show_all(book: AddressBook):
    return book

def show_all_birthdays(book: AddressBook):
    return book.get_upcoming_birthdays()

commands_list = """
Commands:
1. add [name] [phone]: Add a new contact with a name and phone number, or update the phone number for an existing contact.
2. change [name] [new phone]: Change the phone number for the specified contact.
3. phone [name]: Show the phone number for the specified contact.
4. all: Show all contacts in the address book.
5. add-birthday [name] [date of birth]: Add the date of birth for the specified contact.
6. show-birthday [name]: Show the date of birth for the specified contact.
7. birthdays: Show upcoming birthdays within the next week.
8. hello: Receive a greeting from the bot.
9. close or exit: Close the program.
10. commands: Print the list of commands.
"""


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    print(commands_list)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(show_all_birthdays(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book)) 



        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
