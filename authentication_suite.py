#!/usr/bin/python3
# -*- encoding=utf8 -*-

import pytest
from selenium import webdriver

from pytest_final_test.FinalProjectQA.page_classes.authentication_page import AuthPage
from pytest_final_test.FinalProjectQA.page_classes.registration_page import RegistrationPage


@pytest.mark.parametrize("email", ["<correct>", "<wrong>"], ids=["валидный адрес", "невалидный адрес"])
@pytest.mark.parametrize("password", ["<correct>", "<wrong>"], ids=["валидный пароль", "неправильный пароль"])
def test_rostelekom_page_email(email, password):
    """Проверка входа по адресу электронной почты. Вместо "<correct>" ввести валидное значение,
    вместо "wrong" - любое незарегистрированное"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = AuthPage(web_browser)

    page.username.send_keys(email)

    page.password.send_keys(password)

    web_browser.implicitly_wait(3)
    page.enter_button.click()
    if email == "correct" and password == "correct":
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    page.close()


@pytest.mark.parametrize("phone", ["<correct>", "<wrong>"], ids=["валидный адрес", "невалидный адрес"])
@pytest.mark.parametrize("password", ["<correct>", "<wrong>"], ids=["валидный пароль", "неправильный пароль"])
def test_rostelekom_page_phone(phone, password):
    """Проверка входа по номеру телефона. Вместо "<correct>" подставить валидное значение,
    вместо "wrong" - любое незарегистрированное"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = AuthPage(web_browser)

    page.username.send_keys(phone)
    web_browser.implicitly_wait(3)
    page.password.send_keys(password)

    web_browser.implicitly_wait(3)
    page.enter_button.click()
    if phone == "correct" and password == "correct":
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    # print(page.screenshot('current_page.png'))
    page.close()


@pytest.mark.parametrize("login", ["<correct>", "<wrong>"], ids=["валидный адрес", "невалидный адрес"])
@pytest.mark.parametrize("password", ["<correct>", "<wrong>"], ids=["валидный пароль", "неправильный пароль"])
def test_rostelekom_page_login(login, password):
    """Проверка входа по логину.  Вместо "<correct>" подставить валидное значение,
    вместо "wrong" - любое незарегистрированное"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = AuthPage(web_browser)

    page.username.send_keys(login)
    web_browser.implicitly_wait(3)
    page.password.send_keys(password)

    web_browser.implicitly_wait(3)
    page.enter_button.click()
    if login == "correct" and password == "correct":
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    # print(page.screenshot('current_page.png'))
    page.close()


@pytest.mark.parametrize("account", ["<correct>", "<wrong>"], ids=["валидный адрес", "невалидный адрес"])
@pytest.mark.parametrize("password", ["<correct>", "<wrong>"], ids=["валидный пароль", "неправильный пароль"])
def test_rostelekom_page_account(account, password):
    """Проверка входа по номеру лицевого счёта.  Вместо "<correct>" подставить валидное значение,
    вместо "wrong" - любое незарегистрированное"""
    web_browser = webdriver.Chrome('/chromedriver.exe')
    page = AuthPage(web_browser)

    page.username.send_keys(account)
    web_browser.implicitly_wait(3)
    page.password.send_keys(password)

    web_browser.implicitly_wait(3)
    page.enter_button.click()
    if account == "correct" and password == "correct":
        assert page.get_current_url() == 'https://start.rt.ru/?tab=main'
    else:
        assert page.message.get_text() == 'Неверный логин или пароль'
    # print(page.screenshot('current_page.png'))
    page.close()


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
    page.first_name_field.send_keys("first_name")
    page.data_field.click()
    assert page.warning_message_names.get_text() == ''
    print(page.warning_message_names.get_text())
