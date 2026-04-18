from view import View
from model import Model

class Controller:
    def __init__(self, filename) -> None:
        """
        Cоздаем экземпляры класса для взаимодействия  по mvc
        :param filename:
        """
        self.view = View()
        self.model = Model(filename)

    def add(self) -> str:
        """
        Тут получаем  из view введеные параметрами.
        Дергаем метод add_contact из модели и получаем из него id
        Возвращаем строку которую в дальнейшем будем показывать пользователю

        :return:
        """
        name = self.view.get_name()
        phone = self.view.get_phone()
        comment = self.view.get_comment()
        contact_id = self.model.add_contact(name, phone, comment)
        return f'Добавлен контакт с id {contact_id},{name},{phone},{comment}'

    def show_all_contacts(self):
        """
        Получаем список контактов из модели
        Записываем в переменные лист листов контактов
        передаем методу вьюшки для показа контактов

        :return:
        """
        contacts = self.model.all_contacts()
        self.view.show_all_contacts(contacts)

    def run(self):
        self.view.show_menu()
        choice = self.view.get_choice()
        if choice == '1':
            contacts = self.model.all_contacts()
            self.view.show_all_contacts(contacts)
        elif choice == '2':
            information = self.add()
            self.view.show_message(information)
        elif choice not in ['1','2']:
            print('Действие выбрано неверно')

