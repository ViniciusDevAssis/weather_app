import flet as ft

def main(page: ft.Page):
     
     page.window.full_screen = True
     page.horizontal_alignment = "center"
     page.vertical_alignment = "center"

     main_container = ft.Container(
          bgcolor="#3f6cb7",
          border_radius=10,
          expand=True,
          content=ft.Column(
               alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
          )
     )

     top_container = ft.Container(
          # bgcolor="white",
          height=100,
          padding=10,
          content=ft.Row(
               
          )
     )

     local_search = ft.TextField(
          bgcolor="white",
          border_color="white",
          border_radius=10,
          width=page.window.width * 0.90,
          hint_text="Enter the city and country name",
          hint_style=ft.TextStyle(
               size=14,
               color="black"
          ),
          text_align=ft.TextAlign.CENTER,
          text_style=ft.TextStyle(
               size=14,
               color="black"
          ),
          expand=True,
          value="Feira de Santana, BR"
     )

     btn_search = ft.IconButton(
          icon="Search"
     )



     main_container.content.controls.append(top_container)
     top_container.content.controls.append(local_search)
     top_container.content.controls.append(btn_search)

     page.add(main_container)

ft.app(target=main)