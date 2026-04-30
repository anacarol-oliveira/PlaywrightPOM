from playwright.sync_api import Page, expect

class CommonPage:
    def __init__(self, page: Page):
        self.page = page
        self.back_home_button = page.get_by_role("button", name="Voltar para a Home")

    def assert_text(self, text):
        self.page.get_by_text(text).wait_for()
        expect(self.page.get_by_text(text)).to_be_visible()

    def back_home(self):
        self.back_home_button.click()