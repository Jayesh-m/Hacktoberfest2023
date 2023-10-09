class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name not in self.contacts:
            self.contacts[name] = phone
            print(f"Contact '{name}' added successfully!")
        else:
            print(f"Contact '{name}' already exists. Use 'Update Contact' to modify it.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact '{name}': {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter the contact name: ")
            phone = input("Enter the contact phone number: ")
            contact_manager.add_contact(name, phone)
        elif choice == '2':
            contact_manager.list_contacts()
        elif choice == '3':
            name = input("Enter the contact name to search: ")
            contact_manager.search_contact(name)
        elif choice == '4':
            name = input("Enter the contact name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
