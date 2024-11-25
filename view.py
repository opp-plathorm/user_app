import flet as ft
from designer import color
from pages import login

def ViewsHendler(page:ft.Page):
    return {
        "/":ft.View(
            route="/",
            controls=[
                login.Login(page=page)
            ],
            bgcolor=color[2]
        )
    }