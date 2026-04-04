from unittest import result

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
