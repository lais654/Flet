import flet as ft
 
def main(page:ft.Page):
    page.title = "Calculadora"
    numero1=ft.TextField(label="Primeiro número")
    numero2=ft.TextField(label="Segundo número")
    
    resultado=ft.Text("Resultado:")
    def calcular():
        float(numero1.value)
        float(numero2.value)


        page.add(numero1, numero2, resultado)
ft.app(target=main)