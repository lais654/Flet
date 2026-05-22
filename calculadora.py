import flet as ft
def main(page:ft.Page):

    page.title = "Calculadora"
    numero1=ft.TextField(label="Primeiro número")
    numero2=ft.TextField(label="Segundo número")
    
    resultado=ft.Text("Resultado:")

    def calcular(e):
        n1=float(numero1.value)
        n2=float(numero2.value)

        operacao = operacoes.value

        if operacao == "+":
            conta=n1+n2
        elif operacao == "-":
            conta=n1-n2
        elif operacao == "*":
            conta=n1 * n2
        elif operacao == "/":
            conta=n1/n2
        
        resultado = f"resultado:{conta}"
        page.update()

    operacoes = ft.Dropdown(
        label="Escolha a operação",
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/"),
            ]

        )

    Botao = ft.ElevatedButton(
        "Calcular",
        on_click=calcular
    )

    page.add(numero1, numero2, resultado, operacoes, Botao)
ft.app(target=main) 
