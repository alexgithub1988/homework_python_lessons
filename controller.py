from view import View
from model import Model

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def add(self):
        name = self.view.get_name()
        phone = self.view.get_phone()
        comment = self.view.get_comment()
        contact_id = self.model.add_contact(name, phone, comment)
        return f'Добавлен контакт с id {contact_id},{name},{phone},{comment}'

    def show_all_contacts(self):
        contacts = self.model.add_contact()
        list_of_contacts = self.model.all_contacts(contacts)
        return list_of_contacts
    def run(self):
        self.view.show_menu()
        choice = self.view.get_choice()
        if choice == '1':
            contacts = self.model.all_contacts()
            self.view.show_all_contacts(contacts)