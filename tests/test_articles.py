from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_all_tabs_clickable(browser, base_url, wait):
    browser.get(base_url)
    # Считаем сколько вкладок на странице
    tabs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.tab-link")))
    assert "active" in tabs[0].get_attribute("class"), 'Первая вкладка должна быть активной при открытии'
    tabs_count = len(tabs)

    for i in range(tabs_count):
        # Переполучаем список после каждого перехода
        tabs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.tab-link")))
        tab = tabs[i]
        tab_name = tab.text
        expected_href = tab.get_attribute("href")

        wait.until(EC.element_to_be_clickable(tab))
        tab.click()

        # Ждём, пока нужная вкладка получит класс active
        wait.until(
            lambda d, href=expected_href:
            d.find_element(By.CSS_SELECTOR, "a.tab-link.active").get_attribute("href") == href
        )

        clicked_tab = browser.find_element(By.CSS_SELECTOR, "a.tab-link.active")
        assert "active" in clicked_tab.get_attribute("class"), \
            f'Вкладка "{tab_name}" должна иметь класс active'

        assert browser.current_url == expected_href, \
            f'URL после клика на "{tab_name}" должен быть {expected_href}'

        active_tabs = browser.find_elements(By.CSS_SELECTOR, "a.tab-link.active")
        assert len(active_tabs) == 1, f'Активна должна быть только одна вкладка, найдено: {len(active_tabs)}'