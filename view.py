class View:
    @staticmethod
    def show_menu() -> None:
        """
        Список действий
        :return:
        """
        print("1.Показать все")
        print("2.Добавить контакт")
        print("3.Удалить контакт")
        print("4.Перезаписать контакт")
        print("5.Найти контакт по вхождению в имя")
        print("6.Найти контакт по вхождению телефона")
        print("7.Найти контакт по вхождению комментария")
        print("8.Найти контакт точно по имени")
        print("9.Найти контакт точно по телефону ")
        print("10. Найти контакт точно по комментарию")
        print("11.Выйти ")

    @staticmethod
    def get_choice() -> str:
        """
        Выбираем действие пользователя
        возвращаем выбор
        :return:
        """
        choice = input("Выберите действие: ")
        return choice

    @staticmethod
    def get_name() -> str:
        """Получаем имя
        :return: возвращаем имя в виде строки"""
        name = input("Введите имя: ")
        return name

    @staticmethod
    def get_phone() -> str:
        """Получаем телефон
        :return: возвращаем телефон в виде строки
        """
        phone = input("Введите телефон: ")
        return phone

    @staticmethod
    def get_comment() -> str:
        """
        Получаем комментарий
        :return:  возвращаем комментарий
        """
        comment = input("Введите комментарий: ")
        return comment

    @staticmethod
    def show_message(msg:str) -> None:
        """
        Получаем сообщение и выводим
        :param msg:
        :return:
        """
        print(msg)

    @staticmethod
    def show_contacts(contacts:list) -> None:
        """
        Получаем лист листов с контактами, выводим значения
        :param contacts:
        :return:
        """
        for item in contacts:
            print(f'{item[0]} - {item[1]} - {item[2]} - {item[3]}')

    @staticmethod
    def get_id_contact() -> str:
        """
        Получаем id  для передачи дальше
        :return:
        """
        id = input("Введите id  контакта: ")
        try:
            temp = int(id)
            del temp
            return id
        except:
            print("Нужно ввести числовое значение")





