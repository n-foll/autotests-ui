from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")
    registretion_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registretion_username_input.fill("username")
    registretion_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registretion_password_input.fill("password")
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    page.wait_for_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")  #дожидаемся перехода на страницу по ссылке
    dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_header).to_be_visible()
    page.wait_for_timeout(5000)