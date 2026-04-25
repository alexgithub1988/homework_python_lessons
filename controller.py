from view import View
from model import Model
from exceptions import InvalidContactDataError,ContactNotFoundError


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
        try:
            name = self.view.get_name()
            phone = self.view.get_phone()
            comment = self.view.get_comment()
            contact_id = self.model.add_contact(name, phone, comment)
            return f'Добавлен контакт с id {contact_id},{name},{phone},{comment}'

        except InvalidContactDataError as e:
            return str(e)

    def show_all_contacts(self):
        """
        Получаем список контактов из модели
        Записываем в переменные лист листов контактов
        передаем методу вьюшки для показа контактов

        :return:
        """
        contacts = self.model.all_contacts()
        self.view.show_contacts(contacts)

    def run(self) -> None:
        """Метод для запуска """
        while True:
            self.view.show_menu()
            choice = self.view.get_choice()

            if choice == '1':
                contacts = self.model.all_contacts()
                self.view.show_contacts(contacts)
            elif choice == '2':
                information = self.add()
                self.view.show_message(information)
            elif choice == '3':
                id = self.view.get_id_contact()
                try:
                    msg = self.model._delete_contact(id)
                    self.view.show_message(msg)
                except ContactNotFoundError as e:
                    self.view.show_message(str(e))
            elif choice == '4':
                id = self.view.get_id_contact()
                try:
                    name = self.view.get_name()
                    phone = self.view.get_phone()
                    comment = self.view.get_comment()
                    msg = self.model._update_contact(id, name, phone, comment)
                    self.view.show_message(msg)
                except ContactNotFoundError as e:
                    self.view.show_message(str(e))
            elif choice == '5':
                name = self.view.get_name()
                search_list = self.model._search_in_name(name)
                if len(search_list) > 0:
                    msg = 'Найденые контакты'
                    self.view.show_message(msg)
                    self.view.show_contacts(search_list)

                else:
                    msg = 'Контакты не найдены'
                    self.view.show_message(msg)
            elif choice == '6':
                phone = self.view.get_phone()
                search_list = self.model._search_in_phone(phone)
                if len(search_list) > 0:
                    msg = 'Найдены  контакты'
                    self.view.show_message(msg)
                    self.view.show_contacts(search_list)
                else:
                    msg = 'Контакты не найдены'
                    self.view.show_message(msg)
            elif choice == '7':
                comment = self.view.get_comment()
                search_list = self.model._search_in_comment(comment)
                if len(search_list) > 0:
                    msg = 'Найдены  контакты'
                    self.view.show_message(msg)
                    self.view.show_contacts(search_list)
                else:
                    msg = 'Контакты не найдены'
                    self.view.show_message(msg)

            elif choice == '8':
                name = self.view.get_name()
                search_list = self.model._search_name(name)
                if len(search_list) > 0:
                    msg = 'Найдены  контакты'
                    self.view.show_message(msg)
                    self.view.show_contacts(search_list)
                else:
                    msg = 'Контакты не найдены'
                    self.view.show_message(msg)
            elif choice == '9':
                phone = self.view.get_phone()
                search_list = self.model._search_phone(phone)
                if len(search_list) > 0:
                    msg = 'Найдены  контакты'
                    self.view.show_message(msg)
                    self.view.show_contacts(search_list)
                else:
                    msg = 'Контакты не найдены'
                    self.view.show_message(msg)
            elif choice == '10':
                comment = self.view.get_comment()
                search_list = self.model._search_comment(comment)
                if len(search_list) > 0:
                    msg = 'Найдены  контакты'
                    self.view.show_message(msg)
                    self.view.show_contacts(search_list)
                else:
                    msg = 'Контакты не найдены'
                    self.view.show_message(msg)

            elif choice == '11':
                break
            elif choice not in ['1','2','3','4','5', '6', '7', '8', '9','10','11']:
                print('Действие выбрано неверно')



