__author__ = "Chris"

def add_contact(contacts, name, number, *args):
    """Adds a contact to the contacts dictionary"""
    
    
    # attribute types are all on the same index in every contact
    value = [number]
    for attr in args:
        value.append(attr)
    contacts[name] = value


def del_contact(contacts, name):
    """Removes a contact from the contacts dictionary"""
    del contacts[name] # remove contact from dictionary (if it exists)
    

def edit_contact(contacts, name, number, *args):
    """Edits the contacts dictionary"""
    
    
    value = contacts.get(name)
    if value[0] != "":  # string empty if u dont want to change the value
        value[0] = number
        
    for i, attr in enumerate (args):
        if i + 2 >= len(value) and attr != "":  # if there is no attribute at this index 
            value.append(attr)
        elif attr != "":  # string empty if u dont want to change the value
            value[i + 1] = attr
                

def list_contacts(contacts):
    """Lists all contacts in the contacts dictionary"""

    for key in contacts.keys():
        print(key)  # print all names 
        

def show_contact(contacts, name):
    """Shows a contact from the contacts dictionary"""
    
    for value in contacts.get(name):
        print(value)  # print all values of the contact
        

if __name__ == "__main__":
    contacts = {}
    add_contact(contacts, "kevin", "123456789")  # add some contacts
    
    try:
        add_contact(contacts, kevin, "123456789")  # NameError: name 'kevin' is not defined
    except:
        print("NameError: name 'kevin' is not defined")
        
    del_contact(contacts, "kevin")  # remove a contact
    
    try:
        del_contact(contacts, kevin)  # NameError: name 'kevin' is not defined 
    except:
        print("NameError: name 'kevin' is not defined")
        
    try:
        del_contact(contacts, "123456789")  # KeyError: '123456789'
    except:
        print("KeyError: '123456789'")
        
    try:
        show_contact(contacts, "kevin")  # KeyError: 'kevin'
    except:
        print("KeyError: 'kevin'")
        
    add_contact(contacts, "kevin", "123456789", "kevin@gmail.com")  # add contact with an attribute
    show_contact(contacts, "kevin")  # print contact
    add_contact(contacts, "Aure", "987654321")  # add another contact
    list_contacts(contacts)  # print all contacts
    edit_contact(contacts, "kevin", "123456789")  # edit contact
    