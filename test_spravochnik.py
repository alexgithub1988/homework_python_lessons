from unittest import result
from unittest.mock import patch

import pytest
import os
from spravocnik import Spravochnik

test_filename = 'test.csv'
id_counter_file = 'id.txt'
@pytest.fixture
def cleaning():
    if os.path.exists(test_filename):
        os.remove(test_filename)

    if  os.path.exists(id_counter_file):
        os.remove(id_counter_file)
    yield

    if os.path.exists(test_filename):
        os.remove(test_filename)
    if os.path.exists(id_counter_file):
        os.remove(id_counter_file)

@pytest.fixture
def create_test_object():
    test = Spravochnik(test_filename)
    return test






@pytest.fixture
def prepare_data(create_test_object):
    create_test_object._add_number("Vasya","123","test_user1")
    create_test_object._add_number("Petya", "111", "test_user2")
    create_test_object._add_number("Ivan", "222", "test_user3")
    create_test_object._add_number("Vova", "333", "test_user4")
    return create_test_object





@pytest.mark.parametrize("name,phone,comment",
                         [("Vasya",'123','friend'),
                          ("Vova",'555','work'),
                          ("Alex","444",""),
                          ])
def test_add_number(cleaning, name, phone, comment):
    test = Spravochnik(test_filename)
    test._add_number(name,phone,comment)
    assert test.buffer[0][0] == 1
    assert test.buffer[0][1] == name
    assert test.buffer[0][2] == phone
    assert test.buffer[0][3] == comment



@pytest.mark.parametrize("name,phone,comment",
                             [("", '123', 'friend'),
                              ("Vova", "", 'work'),

])
def test_add_number_negative(cleaning, name, phone, comment):
    test = Spravochnik(test_filename)
    result = test._add_number(name,phone,comment)
    assert result == None

@pytest.mark.parametrize("id,new_name,new_phone,new_comment",[
    (1,"Vasya","452","changed"),
    (2,"Dima","555","changed"),
    (3,"Alex","333","changed"),
    (4,"Change","999","changed")

])
def test_update_number(cleaning,prepare_data,id,new_name,new_phone,new_comment):
    """
    1.Чистим данные перед тестами, фикстура cleaning
    2.Подготавливаем дату, фикстура prepare_data
    3.Мокаем input() через unittest patch
    4. Проверяем что в буфере новые значения

    :param cleaning: Чистим дату
    :param prepare_data: Подготавливаем данные
    :param id: id контакта который нужно поменять
    :param new_name: Новое имя
    :param new_phone: Новый телефон
    :param new_comment: Новый комментарий
    :return: None
    """
    with patch("builtins.input",side_effect=[id,new_name,new_phone,new_comment]):
        prepare_data._update_contact()
    index = id -1
    assert prepare_data.buffer[index][1] == new_name
    assert prepare_data.buffer[index][2] == new_phone
    assert prepare_data.buffer[index][3] == new_comment

