import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture  #Декоратор, который указывает на то, что фикстура
def browser():

    driver = webdriver.Chrome()

    yield driver # Возвращаем драйвер в тест

    driver.quit()

@pytest.fixture
def base_url():
    return " https://habr.com/ru/articles/"

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)