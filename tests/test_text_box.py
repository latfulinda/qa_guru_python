import time

from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def given_opened_text_box():
    browser.open('/automation-practice-form')
    s('footer').perform(command.js.remove)
    s('#close-fixedban').perform(command.js.remove)


def test_submit_form():
    given_opened_text_box()

    s('#firstName').type('dima')
    s('#lastName').type('latfulin')
    s('#userEmail').type('latfulinda@gg.com')
    s('#gender-radio-1').double_click()
    s('#userNumber').type('+7999000222')
    s('#dateOfBirthInput').type('17 Jun 2023')
    s('#subjectsInput').type('test practice form')
    s('#hobbies-checkbox-1').double_click()
    s('#hobbies-checkbox-2').double_click()
    # s('uploadPicture').type('+7999000222')
    # s('currentAddress').type('+7999000222')
    s('#state').double_click()
    # s('#react-select-3-input').click()

    s('#city').double_click()
    # s('#react-select-3-input').double_click()
    time.sleep(10)
    s('#submit').double_click()

    # ss('#output p').should(have.texts(
    #     'yasha',
    #     'yashaka@gmail.com',
    #     'Earth',
    #     'Universe & abroad',
    # ))
