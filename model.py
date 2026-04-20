import csv
from pathlib import Path


class Model:
    def __init__(self, filename: str) -> None:
        """


        Логика пока что следующая
        1.Инициализируем имя файла
        2.Создаем буфер с контактами
        3.Если файл не существует устанавливаем переменную с id  в 1
        4 Далее (файл не существует) проверяем что имя файла передано
         в csv формате и если да
        то:
           Открываем файл в режиме записи через контекст менеджер (по факту создаем файл)
           и записываем в него хедер
        если нет:
           поднимаем исключение
        Если файл существуют проходимся по нему циклом и добавляем в лист с контактами

        :param filename:
        """
        self.filename = filename
        self.contacts = []
        if not self._check_exist_file():
            self.next_id = 1
            if self._check_csv_format():
                with open(self.filename, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["id", "name", "phone", "comment"])
            else:
                raise Exception('Формат файла не csv')
        else:
            if self._check_csv_format():
                reader = self._reader()
                if reader[-1][0] == 'id' :
                    self.next_id = 1
                else:
                    self.next_id = int(reader[-1][0])
                for row in reader:
                    self.contacts.append(row)


    def add_contact(self,name:str,phone:str,comment:str ) -> int:
        """
        Метод получает параметры для добавления в виде строк (получаем значения через input())
        Добовляем список значений в контакты
        инкриментим id
        возрващаем значение id   будет использоваться в дальнейшем
        :param name:
        :param phone:
        :param comment:
        :return:
        """
        self.next_id += 1
        self.contacts.append([self.next_id,name,phone,comment])
        self._save_to_csv()

        return self.next_id

    def all_contacts(self) -> list:
        """Возвращаем список с контактами"""
        return self.contacts

    def _check_csv_format(self) -> bool:
        """
        Проверка на csv  формат
        :return:
        """
        if self.filename.endswith('.csv'):
            return True
        else:
            return False

    def _check_exist_file(self) -> bool:
        """
        Проверка существует ли файл по указаному пути
        :return:
        """
        if Path(self.filename).exists():
            return True
        else:
            return False
    def _reader(self) -> list:
        """
        Метод ридера из csv файла
        :return:  возвращает лист значений построчно
        """
        with open(self.filename, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            return list(reader)

    def _save_to_csv(self):
        """
        Сохраняем из буфера в файл
        :return:
        """
        with open(self.filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.contacts)

    def _check_id(self,id:str) -> bool:
        """
        Проверка есть ли id
        :return:
        """
        flag = False
        for row in self.contacts:
            if row[0] == id:
                flag = True
        return flag


    def _delete_contact(self,id: str) -> str:
        """
        перезаписываем значения за исключением удаляемого id
        + делаем проверки на некоторые неправильные id
        :param id:
        :return:
        """
        if int(id) > int(self.contacts[-1][0]):
            return f'Введен id  превышающий максимальный'
        flag = self._check_id(id)
        if flag:
            pass
        else:
            return f'Данного id  нет в контактах'

        temp_list = []
        for row in self.contacts:
            if row[0] == id:
                pass
            else:
                temp_list.append(row)
        self.contacts = temp_list.copy()
        self._save_to_csv()
        flag = self._check_id(id)
        if flag:
            return f'удаление прошло успешно'
        else:
            return f'при удалении что то пошло не так'

    def _update_contact(self,id:str,name:str,phone:str,comment:str) -> str:
        flag = self._check_id(id)
        if flag:
            pass
        else:
            return 'Данного id  нет в котактах'
        temp = []
        for i in self.contacts:
            if i[0] == id:
                temp.append([id,name,phone,comment])
            else:
                temp.append(i)
        self.contacts = temp.copy()
        self._save_to_csv()
        return 'Контакт обновлен'

    def _search_in_name(self,name:str) -> list:
        """
        Получаем имя возвращаем лист который покажем пользователю после обработки
        :param name:
        :return:
        """
        temp_list = []
        for row in self.contacts:

            if name.lower() in row[1].lower():
                temp_list.append(row)

        return temp_list

    def _search_in_phone(self,phone:str) -> list:
        """получаем телефон отдаем лист вхождений"""
        temp_list = []
        for row in self.contacts:

            if phone.lower() in row[2].lower():
                temp_list.append(row)

        return temp_list

    def _search_in_comment(self,comment:str) -> list:
        """
        Получаем часть комментария выводим совпадения
        :param comment:
        :return:
        """
        temp_list = []
        for row in self.contacts:

            if comment.lower() in row[3].lower():
                temp_list.append(row)

        return temp_list

    def _search_name(self,name:str) -> list:
        """
        Получаем точное имя, отдаем вхождения
        :param name:
        :return:
        """
        temp_list = []
        for row in self.contacts:

            if name.lower() == row[1].lower():
                temp_list.append(row)
        return temp_list

    def _search_phone(self, phone: str) -> list:
        temp_list = []
        for row in self.contacts:

                if phone.lower() == row[2].lower():
                    temp_list.append(row)
        return temp_list

    def _search_comment(self,comment:str) -> list:
        """
        Получаем точный  комментария отдаем значения
        :param comment:
        :return:
        """
        temp_list = []
        for row in self.contacts:

            if comment.lower() == row[3].lower():
                temp_list.append(row)
        return temp_list




