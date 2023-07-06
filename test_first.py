import pytest

"""
pytest --collect-only список тестов которые запустятся
"""


@pytest.fixture()
def before_each():
    print("Called before each test")

"""
scope определяет к каким тестам использовать фикстуру
autouse позволяет вызвать фикстуру неявно 
"""
@pytest.fixture(scope='session', autouse=True)
def init_browser(request):
    print("Browser init " + request.node.name)


@pytest.fixture()
def message():
    return "This is message"


""" yield это выполнение теста, а все что после будет после теста"""
@pytest.fixture()
def client():
    client =123
    print("Подготовка клиента")
    yield client
    print("А теперь удаляем клиента")


def test_mobile_page(chrome_mobile):
    assert 1 == 1


def test_first(before_each):
    pass


def test_second(message):
    print(message)
    assert "message" in message


def test_client(client):
    assert client == 121
