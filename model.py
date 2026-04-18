class Model:
    def __init__(self):
        self.contacts = []
        self.next_id = 1

    def add_contact(self,name,phone,comment ):
        self.contacts.append([self.next_id,name,phone,comment])
        self.next_id += 1

    def all_contacts(self):
        return self.contacts