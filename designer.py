import flet as ft

color = [
    "#f0ece2",
    "#dfd3c3",
    "#c7b198",
    "#596e79",
    "#7E93A0FF"
]

class Field(ft.TextField):
    def __init__(self,_label_:str="",_password_:bool=False):
        super().__init__(
            border_color=color[3],
            color=color[3],
            text_size=24,
            label=_label_,
            password=_password_,
            can_reveal_password=_password_,
            label_style=ft.TextStyle(
                color=color[3],
                size=24
            ),
        )
        
class but(ft.ElevatedButton):
    def __init__(self,text:str=""):
        super().__init__(
            color=color[3],
            bgcolor=color[1],
            text=text,
            style=ft.ButtonStyle(
                overlay_color=color[4],
                text_style=ft.TextStyle(
                    size=24
                )
            )
        )