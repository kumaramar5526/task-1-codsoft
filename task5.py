class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")
        
    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("\nContacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name} | Phone: {contact.phone_number}")
    
    def search_contact(self, keyword):
        matching_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                matching_contacts.append(contact)
        if matching_contacts:
            print("\nMatching Contacts:")
            for index, contact in enumerate(matching_contacts, start=1):
                print(f"{index}. Name: {contact.name} | Phone: {contact.phone_number}")
        else:
            print("No matching contacts found.")
    
    def update_contact(self, index, new_contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")
            
    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact '{deleted_contact.name}' deleted successfully!")
        else:
            print("Invalid contact index.")

def main():
    contact_book = ContactBook()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        elif choice == "4":
            index = int(input("Enter index of contact to update: "))
            name = input("Enter updated name: ")
            phone_number = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            address = input("Enter updated address: ")
            updated_contact = Contact(name, phone_number, email, address)
            contact_book.update_contact(index, updated_contact)
        elif choice == "5":
            index = int(input("Enter index of contact to delete: "))
            contact_book.delete_contact(index)
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
