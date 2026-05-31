import flet as ft

def main(page):

    def login(e):
        erro = False
        if not entrada_nome.value:
            entrada_nome.error = "Por favor preencha seu nome."
            erro = True
        else:
            entrada_nome.error = None

        if not entrada_senha.value:
            entrada_senha.error = "Campo de senha obrigatório."
            erro = True
        else:
            entrada_senha.error = None
        
        page.update()

        if erro:
            return
        
        nome = entrada_nome.value
        senha = entrada_senha.value
        print(f"Nome: {nome}\nSenha: {senha}")
        page.clean()
        page.add(
            ft.Text(f"Olá, {nome}\nSeja bem-vindo(a) a nossa aplicação!")
            )
        pass

    entrada_nome = ft.TextField(
        label="Digite o seu nome",
        hint_text="Exemplo: Jorge Silva..."
        )
    entrada_senha = ft.TextField(
        label="Digite a sua senha",
        hint_text="Mínimo 8 caracteres"
        )
    page.add(
        entrada_nome,
        entrada_senha,
        ft.Button("Clique em mim", on_click=login)
    )
    pass

ft.run(main)