import os
from controller import Controller
from exceptions import InvalidContactDataError,ContactNotFoundError
import pytest
from model import Model
from pathlib import Path



test_file = 'test.csv'

@pytest.fixture
def cleanup():
    """
    фикстура для подготовки и очистки
    :return:
    """
    model = Model(test_file)
    yield model

    if Path(test_file).exists():
        os.remove(test_file)

def test_file_created(cleanup):
    """
    Тестируем создание файла
    :param cleanup:
    :return:
    """
    assert Path(test_file).exists()

@pytest.fixture
def create_data(cleanup):
    """
    Подготавливаем данные
    :param cleanup:
    :return:
    """
    cleanup.add_contact("David", "444", "test1")
    cleanup.add_contact("Vasya", "444", "test2")
    cleanup.add_contact("Vasya", "444", "test3")
    return cleanup


@pytest.mark.parametrize("name,phone,comment,expected_id", [
    ("David", "444", "", 1),
    ("Vasya", "", "friend", InvalidContactDataError),
    ("", "456", "work", InvalidContactDataError),

])
def test_empty_parametrs(cleanup, name, phone, comment, expected_id):
    """
    Проверяем введение пустого поля
    :param cleanup:
    :param name:
    :param phone:
    :param comment:
    :param expected_id:
    :return:
    """
    if expected_id == InvalidContactDataError:
        with pytest.raises(InvalidContactDataError):
            cleanup.add_contact(name, phone, comment)
    else:
        contact_id = cleanup.add_contact(name,phone,comment)
        assert contact_id == expected_id


def test_add_contact_sequence(cleanup):
    """
    Проверяем сиквенс увеличения id
    :param cleanup:
    :return:
    """
    id_1 = cleanup.add_contact("David", "444", "test1")
    id_2 = cleanup.add_contact("Vasya", "444", "test2")
    id_3 = cleanup.add_contact("Vasya", "444", "test3")
    assert id_1 == 1
    assert id_2 == 2
    assert id_3 == 3


def test_adding_contacts(create_data):
    "Проверяем добавление контактов"
    assert create_data.contacts[0][1] == "David"
    assert create_data.contacts[1][2] == "444"
    assert create_data.contacts[2][3] == "test3"

def test_delete_contact(create_data):
    create_data._delete_contact(1)
    assert create_data.contacts[0][1] == "Vasya"
    with pytest.raises(ContactNotFoundError):
        create_data._delete_contact(1)


def test_update_contacts(create_data):
    """
    Проверяем обновление контакта
    :param create_data:
    :return:
    """
    create_data._update_contact(1,"Test1","5678","test2")

    assert create_data.contacts[0][1] == "Test1"
    assert create_data.contacts[0][2] == "5678"
    assert create_data.contacts[0][3] == "test2"

def test_update_contact_not_found(create_data):
    with pytest.raises(ContactNotFoundError):
        create_data._update_contact(999, "New", "000", "none")


def test_search_name(create_data):
    """
    Поиск по имени
    :param create_data:
    :return:
    """
    return_list_test1 = create_data._search_name("David")
    return_list_test2 = create_data._search_name("Ivan")
    assert return_list_test1[0][1] == "David"
    assert return_list_test2 == []


def test_search_in_name(create_data):
    """
    Поиск по вхождению по имени
    :param create_data:
    :return:
    """
    return_list_test1 = create_data._search_in_name("Da")
    return_list_test2 = create_data._search_name("vi")
    assert return_list_test1[0][1] == "David"
    assert return_list_test2 == []

def test_search_phone(create_data):
    """
    Проверяем поиск по телефону
    :param create_data:
    :return:
    """
    return_list_test1 = create_data._search_phone("444")
    return_list_test2 = create_data._search_phone("666")
    assert return_list_test1[0][2] == "444"
    assert return_list_test2 == []



def test_search_in_phone(create_data):
    """
    Проверяем поиск по телефону(по вхождению)
    :param create_data:
    :return:
    """
    return_list_test1 = create_data._search_in_phone("4")
    return_list_test2 = create_data._search_in_phone("666")
    assert return_list_test1[0][2] == "444"
    assert return_list_test2 == []


def test_search_comment(create_data):
    """
    Проверяем поиск из модели
    :param create_data:
    :return:
    """
    return_list_test1 = create_data._search_comment("test1")
    return_list_test2 = create_data._search_comment("test99")
    assert return_list_test1[0][3] == "test1"
    assert return_list_test2 == []

def test_search_in_comment(create_data):
    """
    Проверяем поиск по вхождению из модели
    :param create_data:
    :return:
    """
    return_list_test1 = create_data._search_in_comment("te")
    return_list_test2 = create_data._search_in_comment("test99")
    assert return_list_test1[0][3] == "test1"
    assert return_list_test1[1][3] == "test2"
    assert return_list_test1[2][3] == "test3"
    assert return_list_test2 == []

def test_add(mocker):
    """
    Проверям add   из контроллера
    мокаем ответы с инпута
    создаем фейковые экземпляры
    проверем возвращаемое сообщение
    :param mocker:
    :return:
    """
    fake_model = mocker.MagicMock()
    fake_model.add_contact.return_value = 1
    fake_view =mocker.MagicMock()
    fake_view.get_name.return_value = "David"
    fake_view.get_phone.return_value = "444"
    fake_view.get_comment.return_value = "test1"
    with mocker.patch('controller.Model',return_value=fake_model), mocker.patch('controller.View',return_value=fake_view):
        controller = Controller('test.csv')
        controller.model = fake_model
        controller.view = fake_view
        result = controller.add()
        assert result == (f'Добавлен контакт с id {fake_model.add_contact.return_value},'
                          f'{fake_view.get_name.return_value},'
                          f'{fake_view.get_phone.return_value},'
                          f'{fake_view.get_comment.return_value}')