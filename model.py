import csv
from pathlib import Path


class Model:
    def __init__(self, filename: str) -> None:
        """


        Логика пока что следующая
        1.Инициализируем имя файла
        2.Закидываем в контакты заголовок(header)
        3.Если файл не существует устанавливаем переменную с id  в 1
        4 Далее (файл не существует) проверяем что имя файла передано
         в csv формате и если да
        то:
           Открываем файл в режиме записи через контекст менеджер (по факту создаем файл)
           и записываем в него хедер
        если нет:
           поднимаем исключение

        :param filename:
        """
        self.filename = filename
        self.contacts = [['id','name','phone','contacts']]
        if self._check_exist_file() == False:
            self.next_id = 1
            if self._check_csv_format() == True:
                with open(self.filename, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Id", "name", "phone", "comment"])
            else:
                raise Exception('Формат файла не csv')


    def add_contact(self,name:str,phone:str,comment:str ) -> int:
        """
        Метод получает параметры для добавления в виде строк (получаем значения через input())
        Добовляем список значений в контакты
        инкриментим id
        возрващаем значение id - 1,  будет использоваться в дальнейшем
        :param name:
        :param phone:
        :param comment:
        :return:
        """
        self.contacts.append([self.next_id,name,phone,comment])
        self.next_id+=1

        return self.next_id - 1

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