class View:
    @staticmethod
    def show_menu():
        """
        Список действий
        :return:
        """
        print("1.Показать все")
        print("2.Добавить контакт")
        print("3 Выйти")

    @staticmethod
    def get_choice():
        """
        Выбираем действие пользователя
        возвращаем выбор
        :return:
        """
        choice = input("Выберите действие: ")
        return choice

    @staticmethod
    def get_name():
        name = input("Введите имя: ")
        return name

    @staticmethod
    def get_phone():
        phone = input("Введите телефон: ")
        return phone

    @staticmethod
    def get_comment():
        comment = input("Введите комментарий: ")
        return comment

    @staticmethod
    def show_message(msg):
        print(msg)

    @staticmethod
    def show_all_contacts(contacts):
        for item in contacts:
            print(f'{item[0]} - {item[1]} - {item[2]} - {item[3]}')



