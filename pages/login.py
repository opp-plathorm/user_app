import flet as ft
from designer import TextField, color

class Login(ft.Column):
    def __init__(self, page:ft.Page=None):
        self.login = TextField(label="Login"),
        self.password = TextField(label="Password")
        super().__init__(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            controls=[
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(color=color[1],size=42,value="Copp")
                        ]
                    )
                ),
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.login
                        ]
                    )
                ),
                ft.Container(
                        content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.password
                        ]
                    )
                ),
                ft.Container(

                    content=ft.Row(
                        controls=[]
                    )
                ),
            ]
        )