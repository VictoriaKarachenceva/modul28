#!/usr/bin/python3
# -*- encoding=utf8 -*-

from FinalTask_28.pages.base_page import WebPage
from FinalTask_28.pages.elements import WebElement


class RegistrationPage(WebPage):

    def __init__(self, web_driver):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)
        web_driver.get(url)

    register_link = WebElement(id='kc-register')

    first_name_field = WebElement(xpath='//input[@name="firstName"]')

    last_name_field = WebElement(xpath='//input[@name="lastName"]')

    data_field = WebElement(id='address')

    password_input = WebElement(id='password')

    password_confirm = WebElement(id='password-confirm')

    register_button = WebElement(xpath='//button[@name="register"]')

    warning_message_names = WebElement(xpath='//div[@class="rt-input-container rt-input-container--error"]')

    warning_message_data = WebElement(xpath='//div[@class="rt-input-container rt-input-container--error email-or-phone register-form__address"]')

    warning_message_pass = WebElement(css_selector='div.card-container.register-form-container div.card-container__wrapper div.card-container__content form.register-form div.new-password-container:nth-child(8) div.rt-input-container.rt-input-container--error.new-password-container__confirmed-password:nth-child(2) > span.rt-input-container__meta.rt-input-container__meta--error')
