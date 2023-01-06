#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest
from selenium import webdriver

from pytest_final_test.FinalProjectQA.page_classes.registration_page import RegistrationPage


def generate_string(num):
    return "а" * num


@pytest.mark.parametrize("first_name", ['аа-аа', generate_string(2), generate_string(3), generate_string(15),
                                        generate_string(29), generate_string(30)],
                         ids=['с дефисом', '2 символа', '3 символа', '15 символов', '29 символов', '30 символов'])
def test_first_name_field_positive(first_name):
    """Негативные проверки для поля ввода имени """
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.first_name_field.send_keys(first_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() == ''
    print(page.warning_message_names.get_text())


@pytest.mark.parametrize("first_name", [generate_string(1), generate_string(31), "latin",
                                        "<script>alert('Поле input уязвимо!')</script>", "SELECT*from NAMES"],
                         ids=["1 символ", "31 символ", "латинские буквы", "XSS-инъекция", "SQL-инъекция"])
def test_first_name_field_negative(first_name):
    """Негативные проверки для поля ввода имени """
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.first_name_field.send_keys(first_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() != ''
    page.close()


@pytest.mark.parametrize("last_name", [generate_string(2), generate_string(3), generate_string(15),
                                       generate_string(29), generate_string(30), "аа-аа"],
                         ids=['2 символа', '3 символа', '15 символов', '29 символов', '30 символов', 'с дефисом'])
def test_last_name_field_positive(last_name):
    """Негативные проверки для поля ввода фамилии"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(last_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() == ''
    print(page.warning_message_names.get_text())
    page.close()


@pytest.mark.parametrize("last_name", [generate_string(1), generate_string(31), "latin",
                                       "<script>alert('Поле input уязвимо!')</script>", "SELECT*from NAMES"],
                         ids=['1 символ', '31 символ', 'латинские буквы', 'XSS-инъекция', 'SQL-инъекция'])
def test_last_name_fields_negative(last_name):
    """Негативные проверки для полz ввода фамилии"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.last_name_field.send_keys(last_name)
    page.data_field.click()
    assert page.warning_message_names.get_text() != ''
    print(page.warning_message_names.get_text())
    page.close()


@pytest.mark.parametrize("data", ["example@mail.ru", "+798812345678", "898812345678", "+375123456789"],
                         ids=["корректный формат адреса", "корректный формат рос-телефона",
                              "формат телефона через 8", "корректный формат бел-телефона"])
def test_data_field_positive(data):
    """Позитивные проверки для полей ввода адреса электронной почты или номера телефона"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.data_field.send_keys(data)
    page.password_input.click()
    assert page.warning_message_data.get_text() == ''
    page.close()


@pytest.mark.parametrize("data", ["example2mail.ru", "+79881234567", "+7988123456789", "+37512345678", "+3751234567890",
                                  "<script>alert('Поле input уязвимо!')</script>", "SELECT*from NAMES"],
                         ids=["некорректный формат адреса", "некорректный формат рос-телефона(10 цифр)",
                              "некорректный формат рос-телефона(12 цифр)", "некорректный формат бел-телефона(8 цифр)",
                              "некорректный формат бел-телефона(10 цифр)", "XSS-инъекция", "SQL-инъекция"])
def test_data_field_negative(data):
    """Негативные проверки для полей ввода адреса электронной почты или номера телефона"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.data_field.send_keys(data)
    page.password_input.click()
    assert page.warning_message_data.get_text() != ' '
    page.close()


@pytest.mark.parametrize("pass_word", ["Pa$sword", "Password1", "Password11Password11",
                                       "<script>alert('Поле input уязвимо!')</script>", "SELECT*from NAMES"],
                         ids=["спецсимвол", "заглавная буква и цифра", "20 символов", "XSS-инъекция", "SQL-инъекция"])
def test_password_field_positive(pass_word):
    """Проверка поля ввода пароля"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.password_input.send_keys(pass_word)
    page.password_confirm.click()
    assert page.password_input.get_text() == ''


@pytest.mark.parametrize("password", ["passwor", "password", "password11", "парольпа", "Password11Password111",
                                      "<script>alert('Поле input уязвимо!')</script>", "SELECT*from NAMES"],
                         ids=["менее 8 символов", "нет спецсимвола или цифры", "без заглавной буквы",
                              "символы кириллицы", "более 20 символов", "XSS-инъекция", "SQL-инъекция"])
def test_password_field_negative(password):
    """Проверка поля ввода пароля"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.password_input.send_keys(password)
    page.password_confirm.click()
    assert page.warning_message_pass.get_text() != ' '
    print(page.warning_message_pass.get_text())


@pytest.mark.parametrize("password", ["Password11", "Password1"], ids=["корректный пароль", "некорректный пароль"])
def test_password_confirmed(password):
    """Проверка поля ввода пароля"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = RegistrationPage(web_browser)

    page.register_link.click()
    page.wait_page_loaded()
    page.password_input.send_keys('Password11')
    page.password_confirm.send_keys(password)
    page.register_button.click()
    if password == 'Password11':
        assert page.password_confirm.get_text() == ''
        print(page.password_confirm.get_text())
    else:
        assert page.password_confirm.get_text() != ''
        print(page.password_confirm.get_text())
