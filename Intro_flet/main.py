import flet as ft

def main (pantalla: ft.Page):
    def saludar(e: ft.Event[ft.Button]):
        pantalla.show_dialog(ft.SnackBar(ft.Text("Hola click")))
        
    pantalla.tittle = "Mi primera App con flet😁"
    pantalla.appbar = ft.AppBar(
        title = "Mi App" ,
        bgcolor = ft.Colors.SURFACE_CONTAINER_HIGH,
        actions = [ft.IconButton(ft.Icons.SETTINGS)]
    )
    mensaje = ft.Text("Hola mundo desde Flet!! 🙌")
    boton = ft.Button("Click aquí", on_click = saludar)
    pantalla.add(
        mensaje,
        boton
        )

ft.run(main)



