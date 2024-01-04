#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Contact Information: Store name, phone number, email, and address for each contact.
# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers.
# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.
# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction

contact={}

def display():
    print("Name \t\tContact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    ch=int(input("enter your choice: \n 1.Add new contact \n 2.Search contact \n 3.display contact \n 4.edit contact \n 5.delete contact"))
    if ch==1:
        name=input("Enter contact name: ")
        pno=input("Enter phone number : ")
        email=input("Enter email : ")
        add=input("Enter address: ")
        contact[name]=pno
        
    elif ch==2:
        search_name=input("Enter the contact name:")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("name is not found in the contact list")
    elif ch==3:
        if not contact:
            print("empty contact book")
        else:
            display()
    elif ch==4:
        edit=input("enter the contact name to be edited")
        if edit in contact:
            pnumber=input("enter phone number")
            contact[edit]=pnumber
            print("contact updated")
            display()
        else:
            print("name is not found in the contact book")
    elif ch==5:
        del_contact=input("enter the contact to delete")
        if del_contact in contact:
            confirm=input("do you want to delete contact y/n" )
            if confirm =='y' or confirm=='Y':
                contact.pop(del_contact)
            display()
        else:
            print("name is not found in book")
    else:
        break


# In[ ]:




