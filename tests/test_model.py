import os
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

@pytest.fixture
def create_data(cleanup):
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
    create_data._update_contact(1,"Test1","5678","test2")

    assert create_data.contacts[0][1] == "Test1"
    assert create_data.contacts[0][2] == "5678"
    assert create_data.contacts[0][3] == "test2"


def test_search_name(create_data):
    return_list_test1 = create_data._search_name("David")
    return_list_test2 = create_data._search_name("Ivan")
    assert return_list_test1[0][1] == "David"
    assert return_list_test2 == []

