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

