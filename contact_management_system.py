import re
import os

# User Interface, navigates through each menu
def menu():
    while True:
        print("Welcome to the Contact Management System!\n\nMenu")
        print("1. Add a new contact \n2. Edit an existing contact")
        print("3. Delete a contact \n4. Display all content \n5. Search for a contact \n6. Export contacts to a text file")
        print("7. Quit")
        choice = input("What would you like to do? (1-7) ")

        if choice == '1':
            new_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            log_contacts()
        elif choice == '7':
            print("Thank you for using the Contact Management System. Hope to see you again!")
            quit()
        else:
            print("Invalid choice.")

#Contact Data Storage, use dictionaries as main data structure. Include Name, Phone number, Email address.
contacts = {}

# Menu Actions

#Creates new contact and inserts them into the contacts dictionary
def new_contact():
    print("Add a new contact\n")
    print("Please enter the new contact information below.")
    contact_name = input("Name: ").lower().strip()
    while True:
        contact_phone_number = input("Phone Number: (Separated by '-', eg 123-456-7890)").strip()
        if validate_phone_number(contact_phone_number):
            break
        print("Invalid phone number format. Please enter a valid phone number.")
    while True:
        contact_email_address = input("Email Address: (must have '@')")
        if validate_email(contact_email_address):
            break
        print("Incorrect email format. Please enter a valid email.")
    contacts[contact_name] = {"Phone Number": contact_phone_number, "Email Address": contact_email_address}
    print(contacts)

#Allows the user to edit a contact and update the value in the dictionary
def edit_contact():
    print("Edit a contact")
    chosen_contact = input("Please enter the name of the contact you would like to edit")
    if chosen_contact not in contacts:
        print("Sorry this contact is not in our system")
    else:
        pass

    print(f"Current details of {chosen_contact}: {contacts[chosen_contact]}")
    detail_key = input("Enter what detail you would like to edit (Email Address or Phone Number)")
    updated_value = input("What would you like to change it to? ")
    contacts[chosen_contact][detail_key] = updated_value
    print(f"Updated Contact {chosen_contact}'s Information!")

#Finds the name of the contact that the user wants to delete from the contacts dictionary
def delete_contact():
    print("Delete a contact")
    selected_contact = input("Please enter the name of the contact you would like to delete")
    if selected_contact in contacts:
        del contacts[selected_contact]
        print(f"Deleted {selected_contact}'s Information")

#Displays all the contacts that the user has entered into the dictionary
def display_contacts():
    print("Display contacts")
    for name, details in contacts.items():
        print(f"Name: {name}")
        for info, detail in details.items():
            print(info, ": ", detail)

#Allows the user to search by a name to find a contact
def search_contact():
    print("Search contact")
    searched_name = input("Enter a name you would like to search: ").strip()
    found_contact = {name: details for name, details in contacts.items() if searched_name.lower() in name.lower()}

    if found_contact:
        print(f"Found contact for search '{searched_name}'")
        for name, details in found_contact.items():
            print(f"\nName: {name}")
            for key, value in details.items():
                print(f"{key}: {value}")
    else:
        print(f"No contacts were found with the search of '{searched_name}'")

#Writes a txt file that will store all the contact information inside the dictionary
def log_contacts():
    print("Log contacts")
    try:
        with open("contact_log.txt", "w") as file:
            for name, details in contacts.items():
                file.write(f"Contact: {name}, Email Address: {details['Email Address']}, Phone Number: {details['Phone Number']}\n")
    except:
        pass

#Checks if the email the user entered is valid
def validate_email(contact_email_address):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, contact_email_address) is not None

#Checks if the phone number the user entered is valid
def validate_phone_number(contact_phone_number):
    phone_pattern = r'^(\+?\d{1,3}-)?(\d{3}-)?\d{3}-\d{4}$'
    return re.match(phone_pattern, contact_phone_number) is not None

# Streamline

menu()