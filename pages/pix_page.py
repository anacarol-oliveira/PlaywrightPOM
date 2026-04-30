from playwright.sync_api import Page, expect

class PixPage:
    def __init__(self, page: Page):
        self.page = page
        self.pix_key = page.get_by_role("textbox", name="Chave Pix:")
        self.pix_amount = page.get_by_role("textbox", name="Valor:")
        self.send_pix_button = page.get_by_role("button", name="Enviar Pix")
        self.back_home_button = page.get_by_role("button", name="Voltar para a Home")

    def send_pix(self, key, amount):
        self.pix_key.fill(key)
        self.pix_amount.fill(amount)
        self.send_pix_button.click()

    def assert_pix_realized(self):
        expect(self.page.get_by_text("Transação Realizada com Sucesso!")).to_be_visible()
        expect(self.page.get_by_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações.")).to_be_visible()

    def back_home(self):
        self.back_home_button.click()