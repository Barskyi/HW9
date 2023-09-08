import click

# Словник для зберігання контактів (ім'я - номер телефону)
contacts = {}


# Декоратор input_error для обробки помилок введення користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            click.echo("Contact not found.")
        except ValueError:
            click.echo("Invalid input. Please enter name and phone separated by space.")
        except IndexError:
            click.echo("Invalid input format.")
    return wrapper


# Функція для обробки команди "add"
@input_error
def add(contact_info):
    name, phone = contact_info.split()
    contacts[name] = phone
    click.echo(f"Contact '{name}' added successfully.")


# Функція для обробки команди "change"
@input_error
def change(contact_info):
    name, phone = contact_info.split()
    if name in contacts:
        contacts[name] = phone
        click.echo(f"Phone number for '{name}' updated successfully.")
    else:
        raise KeyError


# Функція для обробки команди "phone"
@input_error
def phone(contact_name):
    phone_number = contacts[contact_name]
    click.echo(f"Phone number for '{contact_name}': {phone_number}")


# Функція для обробки команди "show all"
def show_all():
    if not contacts:
        click.echo("No contacts found.")
    else:
        click.echo("List of contacts:")
        for name, phone in contacts.items():
            click.echo(f"{name}: {phone}")


# Основна функція для взаємодії з користувачем
def main():
    click.echo("Bot is running. Type 'good bye', 'close', or 'exit' to exit.")

    while True:
        user_input = input("Enter a command: ").lower()
        if user_input == "hello":
            click.echo("How can I help you?")
        elif user_input.startswith("add "):
            add(user_input[4:])
        elif user_input.startswith("change "):
            change(user_input[7:])
        elif user_input.startswith("phone "):
            phone(user_input[6:])
        elif user_input == "show all":
            show_all()
        elif user_input in ("good bye", "close", "exit"):
            click.echo("Good bye!")
            break
        else:
            click.echo("Invalid command. Please enter a valid command.")


if __name__ == '__main__':
    main()
