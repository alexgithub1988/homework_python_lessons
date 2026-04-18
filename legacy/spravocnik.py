import csv
from pathlib import Path


class Spravochnik:
    def __init__(self, filename):
        """
        Инициируем справочник

        :param filename: Имя файла который будет использовать справочник
        """
        self.buffer = []
        self.filename = filename
        if self._check_exist_file() == False:
            self.id = 1
            if self._check_csv_format() == True:
                with open(self.filename, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Id", "name", "phone", "comment"])
            else:
                raise Exception('Формат файла не csv')
        else:
            if self._check_csv_format() == True:
                reader = self._reader()
                for row in reader:
                    self.buffer.append(row)
            if Path('id.txt').exists():
                with open('id.txt', 'r', encoding='utf-8') as file:
                    content = file.readline()
                    if content:
                        self.id = int(content)
                    else:
                        self.id = 1
            elif len(self.buffer) == 0:
                self.id = 1
            elif self.buffer[-1][0] == 'Id':
                self.id = 1

            else:

                self.id = int(self.buffer[-1][0]) + 1

    def _update_contact(self) -> None:
        """
        Функция апдейта контакта
        Принимаем пользовательские данные с клавиатуры:
        1) id  контакта
        2) Имя на которое нужно изменить
        3) Телефон на который нужно изменить
        4) Комментарий на котороый нужно изменить
        Если вместо имени, телефона или комментария вводится пустая строка, то
        изменения для этого значения не вносятся
        Сохранение происходит в буфер и в файл

        :return:
        """
        print("Введите id контакта для изменения")
        id = input()
        list_of_ids = []
        temp_list = []
        for ids in self.buffer:
            list_of_ids.append(ids[0])
        if id in list_of_ids:
            print("Введите новое имя")
            name = input()
            print("Введите телефон")
            phone = input()
            print("Введите комментарий")
            comment = input()
            for row in self.buffer:
                if row[0] == id:
                    if name == '':
                        name = row[1]
                    if phone == '':
                        phone = row[2]
                    if comment == '':
                        comment = row[3]

                    temp_list.append([id, name, phone, comment])
                else:
                    temp_list.append(row)
            self.buffer = temp_list.copy()
            self._save_to_csv()

        else:
            print("id отсутсвует в списке")
            return

    def _delete_contact(self):
        print('Введите id который нужно удалить')
        id = input()
        temp_list = []
        for row in self.buffer:
            if row[0] == id:
                pass
            else:
                temp_list.append(row)
        self.buffer = temp_list.copy()
        self._save_to_csv()
        flag = True
        for row in self.buffer:
            if row[0] == id:
                flag = False
        if flag == True:
            print('Удаление успешно завершено')
        else:
            print('При удалении что то пошло не так')

    def _keep_id(self):
        with open("id.txt", 'w', encoding='utf-8') as file:
            last_one = int(self.buffer[-1][0]) + 1
            file.writelines(str(last_one))

    def _check_csv_format(self):
        if self.filename.endswith('.csv'):
            return True
        else:
            return False

    def _check_exist_file(self):
        if Path(self.filename).exists():
            return True
        else:
            return False

    def _reader(self):
        with open(self.filename, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            return list(reader)

    def _save_to_csv(self):
        with open(self.filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.buffer)

    def show_all(self):
        for row in self.buffer:
            print(row[0] + ' ' + row[1] + ' ' + row[2])

    def _add_number(self, name: str, phone: str | int, comment: str)->None:
        """
        Функция делает следующие действия:
        1. Проверяет значения name и phone  на пустую строку
        2. Добавляет введеные значения в буфер
        3. Инкриментит значение id
        4. Сохраняет id  в файл
        5. Сохраняет значения в файл

        :param name: Вводим имя, не может быть пустым
        :param phone: Вводим Телефон, не может быть пустым
        :param comment:  Вводим комментарий
        :return: Функция возвращает None
        """
        if name == "":
            print("Имя не может быть пустым")
            return
        if phone == "":
            print("Телефон не может быть пустым")
            return

        self.buffer.append([str(self.id), name, phone, comment])
        self.id += 1
        self._keep_id()
        self._save_to_csv()

    def _search_id(self):
        print('Введите id')
        id = input()
        flag = False
        for row in self.buffer:
            if row[0] == id:
                print(row[0], row[1], row[2], row[3])
                flag = True
        if flag == False:
            print('Запись не найдена по id')

    def _search_in_name(self):
        print('Введите имя или часть имени')
        name = input()
        flag = False
        for row in self.buffer:
            if name in row[1]:
                print(row[0], row[1], row[2], row[3])
                flag = True
        if flag == False:
            print('Вхождений по именам нет')

    def _search_exact_name(self):
        print('Введите точное имя')
        name = input()
        flag = False
        for row in self.buffer:
            if name == row[1]:
                print(row[0], row[1], row[2], row[3])
                flag = True
        if flag == False:
            print('Имя не найдено')

    def _search_in_phone(self):
        print('Введите телефон или его часть')
        phone = input()
        flag = False
        for row in self.buffer:
            if phone in row[2]:
                print(row[0], row[1], row[2], row[3])
                flag = True
        if flag == False:
            print('Телефон не найден')

    def _search_exact_phone(self):
        print('Введите телефон')
        phone = input()
        flag = False
        for row in self.buffer:
            if phone == row[2]:
                print(row[0], row[1], row[2], row[3])
                flag = True
        if flag == False:
            print('Телефон не найден')

    def menu(self):
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
        action = input()
        if action.lower() == 'exit':
            return

        elif action == '1':
            self.show_all()
        elif action == '2':
            print("Укажите имя")
            name = input()
            print("Укажите телефон")
            phone = input()
            print("Укажите комментарий если нужно")
            comment = input()
            self._add_number(name, phone, comment)
        elif action == '3':
            self._update_contact()
        elif action == '4':
            self._delete_contact()
        elif action == '5':
            self._search_id()
        elif action == '6':
            self._search_in_name()
        elif action == '7':
            self._search_exact_name()
        elif action == '8':
            self._search_in_phone()
        elif action == '9':
            self._search_exact_phone()



        elif action == '10':
            self._save_to_csv()
        else:
            print("Неверный ввод")

if __name__ == '__main__' :
    spravochnik = Spravochnik('test.csv')
    spravochnik.menu()
