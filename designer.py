import flet as ft

color = [
    "#f0ece2",
    "#dfd3c3",
    "#c7b198",
    "#596e79",
    "#7E93A0FF"
]

class TextField(ft.TextField):
    def __init__(self,label:str=""):
        super().__init__(
            border_color=color[3],
            color=color[3],
            text_size=24,
            label=label,
            label_style=ft.TextStyle(
                color=color[3],
                size=24
            ),
        )
