import flet as ft
from designer import Field, color, button
import bcrypt

class Login(ft.Column):
    def __init__(self, page:ft.Page=None):
        self.page = page
        self.login = Field(_label_="Login"),
        self.password = Field(_label_="Password", _password_=True)
        super().__init__(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(color=color[1],size=42,value="Copp")
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.login[0]
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.password
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        button(text="Enter",on_click=self.enter_go_to_next_page)
                    ]
                )
            ]
        )
    def enter_go_to_next_page(self,e):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(self.password.value.encode('utf-8'), salt)
        print(hashed)
        return hashed