def test_003_take_loan(common_page, login_page, home_page, loan_page) -> None:
    login_page.login("user1", "pass1")
    home_page.access_menu("Empréstimos")
    loan_page.take_loan("2.000,00")
    common_page.assert_text("A transação foi concluída com sucesso. Você pode voltar para a página principal e continuar suas operações.")
    common_page.back_home()
    common_page.assert_text("7.000,00")
    home_page.access_menu("Ver Extrato")
    common_page.assert_text("Empréstimo contratado - R$ 2000,00")