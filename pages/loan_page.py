from playwright.sync_api import Page, expect

class LoanPage:
    def __init__(self, page: Page):
        self.page = page
        self.take_loan_button = self.page.get_by_role("button", name="Contratar Empréstimo")

    def select_mount_loan(self, valor):
        self.page.get_by_role("radio", name=f"R$ {valor}").click()

    def take_loan_click(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.take_loan_button.click()

    def take_loan(self, valor):
        self.select_mount_loan(valor)
        self.take_loan_click()
