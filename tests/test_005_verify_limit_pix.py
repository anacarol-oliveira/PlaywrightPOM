def test_005_verify_limit_pix(common_page, login_page, home_page, pix_page) -> None:
    login_page.login("user1", "pass1")
    home_page.access_menu("Fazer Pix")
    pix_page.send_pix("999.999.999-99", "3001,00")
    common_page.assert_text("O valor do Pix não pode ultrapassar R$ 3.000,00. Tente novamente.")