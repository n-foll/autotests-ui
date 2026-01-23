from typing import Pattern
import allure

from playwright.sync_api import Page, expect  # Импортируем класс Page
from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page): 
        self.page = page  # Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # Метод для открытия ссылок
        step = f'Opening the url "{url}"'
        with allure.step(f'Opening the url "{url}"'):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle') #wait_until='networkidle' дожидаемся завершения загрузки всех сетевых запросов перед выполнением последующих шагов.

    def reload(self):  # Метод для перезагрузки страницы
        step = f'Reloading page with url "{self.page.url}"'
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded') #wait_until='domcontentloaded' дожидаемся полного обновления страницы

    # Метод для проверки текущего URL
    def check_current_url(self, expected_url: Pattern[str]):
        step = f' Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)