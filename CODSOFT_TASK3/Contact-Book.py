import json
import os

class ContactBook:
    def __init__(self, storage_file="contacts.json"):
        self.storage_file = storage_file
        self.contacts = self._load_contacts()

    def _load_contacts(self) -> dict:
        """Loads contacts from a JSON file if it exists."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print("⚠️ Error reading storage file. Starting with empty contacts.")
                return {}
        return {}

    def _save_contacts(self):
        """Saves the current contacts dictionary to a JSON file."""
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self, name: str, phone: str, email: str, address: str = ""):
        """Adds a new contact."""
        normalized_name = name.strip()
        if not normalized_name:
            print("❌ Contact name cannot be empty.")
            return

        # Check for case-insensitive duplicate
        if any(existing.lower() == normalized_name.lower() for existing in self.contacts):
            print(f"⚠️ A contact named '{normalized_name}' already exists.")
            return

        self.contacts[normalized_name] = {
            "phone": phone.strip(),
            "email": email.strip(),
            "address": address.strip()
        }
        self._save_contacts()
        print(f"✅ Contact '{normalized_name}' added successfully!")

    def view_all_contacts(self):
        """Displays all contacts in a formatted table."""
        if not self.contacts:
            print("📭 Your contact book is currently empty.")
            return

        print("\n" + "=" * 70)
        print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25}")
        print("-" * 70)
        for name, details in sorted(self.contacts.items()):
            print(f"{name:<20} | {details.get('phone', ''):<15} | {details.get('email', ''):<25}")
        print("=" * 70 + "\n")

    def search_contact(self, query: str):
        """Searches for contacts matching name or phone number."""
        query_lower = query.strip().lower()
        matches = {
            name: info for name, info in self.contacts.items()
            if query_lower in name.lower() or query_lower in info.get("phone", "")
        }

        if not matches:
            print(f"🔍 No contacts found matching '{query}'.")
            return

        print(f"\n🔍 Found {len(matches)} match(es):")
        for name, details in matches.items():
            print(f"  • Name:    {name}")
            print(f"    Phone:   {details.get('phone', 'N/A')}")
            print(f"    Email:   {details.get('email', 'N/A')}")
            print(f"    Address: {details.get('address', 'N/A')}\n")

    def update_contact(self, name: str):
        """Updates details for an existing contact."""
        matched_key = next((k for k in self.contacts if k.lower() == name.strip().lower()), None)
        if not matched_key:
            print(f"❌ Contact '{name}' not found.")
            return

        current = self.contacts[matched_key]
        print(f"\nUpdating '{matched_key}' (press Enter to keep existing value):")
        
        new_phone = input(f"New Phone [{current['phone']}]: ").strip() or current['phone']
        new_email = input(f"New Email [{current['email']}]: ").strip() or current['email']
        new_address = input(f"New Address [{current.get('address', '')}]: ").strip() or current.get('address', '')

        self.contacts[matched_key] = {
            "phone": new_phone,
            "email": new_email,
            "address": new_address
        }
        self._save_contacts()
        print(f"✅ Contact '{matched_key}' updated successfully!")

    def delete_contact(self, name: str):
        """Deletes a contact."""
        matched_key = next((k for k in self.contacts if k.lower() == name.strip().lower()), None)
        if not matched_key:
            print(f"❌ Contact '{name}' not found.")
            return

        del self.contacts[matched_key]
        self._save_contacts()
        print(f"🗑️ Contact '{matched_key}' deleted successfully!")


def main():
    book = ContactBook()

    while True:
        print("\n" + "—" * 30)
        print("📖 --- CONTACT BOOK MENU ---")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("—" * 30)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address/City (optional): ")
            book.add_contact(name, phone, email, address)

        elif choice == "2":
            book.view_all_contacts()

        elif choice == "3":
            query = input("Enter Name or Phone to search: ")
            book.search_contact(query)

        elif choice == "4":
            name = input("Enter the Name of the contact to update: ")
            book.update_contact(name)

        elif choice == "5":
            name = input("Enter the Name of the contact to delete: ")
            book.delete_contact(name)

        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
