import flet as ft
from view import ViewHenler

def main(page:ft.Page):
    def PageLoading(route):
        print(page.route)
        page.views.clear()
        page.views.append(ViewHenler(page=page)[page.route])
        page.update()
        
    page.on_route_change=PageLoading
    page.go("/")
    
ft.app(target=main, assets_dir="assets")