import flet as ft 

def main(page: ft.Page):
    page.title="sentence printer"

    user_input= ft.TextField(label="enter a sentence", width=30000)
    result=ft.Text(size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
    def show_sentence(e):
        result.value=user_input.value or "please enter a sentence"
        page.update()
    submit_button=ft.Button(
        content="show sentence",
        on_click=show_sentence,
    )
    page.add(user_input, submit_button, result)
ft.run(main)