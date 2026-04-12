from typing import Dict


class Viewer:
    """\ Основыные методы для показа и передачи/приема от контроллера
    """

    @staticmethod
    def show_menu() -> None:
        print("Выберите действия")
        print("1. Просмотреть все контакты")
        print("2. Добавить контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Найти контакт по id")
        print("6. Найти контакт по вхождению имени")
        print("7. Найти контакт точно по имени")
        print("8. Найти контакт по вхождению телефона")
        print("9. Найти контакт точно номеру телефона")
        print("10. Сохранить контакты в файл")
        print("Выберите номер действия")
        print("Для выхода напишите exit")

    @staticmethod
    def add_contact_data()->Dict:
        """
        Собираем данные от пользователя,
        возвращаем словарь

        """
        print("Добавление контакта")
        print("Введите имя")
        name = input()
        print('Введите телефон')
        phone = input()
        print("Введите коментарий")
        comment = input()

        return {'name':name,'phone':phone,'comment':comment}

    @staticmethod
    def update_contact_data()->Dict:
        """
        Получаем id и параметры для апдейта
        Возвращаем словарь

        """

        print("Обновление контакта")
        print("Введите id")
        id = input()
        print("Введите имя")
        name = input()
        if name == '':
            name = False
        print('Введите телефон')
        phone = input()
        if phone == '':
            phone = False
        print("Введите коментарий")
        comment = input()
        if comment == '':
            comment = False
        return {'id': id, 'name': name,'phone':phone,'comment':comment}


    @staticmethod
    def delete_contact_data()->Dict:
        """
        Вводим id  возвращаем словарь с id
        :return:
        """
        print("Введите id  контакта")
        id = input()
        return {'id': id}





