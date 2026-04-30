from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def access_menu(self, menu):
        self.page.get_by_role("button", name=f"{menu}").click()
