import flet as ft

def main(page: ft.Page):
     
     page.bgcolor = "white"
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
          height=page.window.height * 0.1,
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

     central_container = ft.Container(
          expand=True,
          height=page.window.height * 0.2,
          padding=10,
          content=ft.Column(
          )
     )

     central_container_row_1 = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          controls=[
               ft.Text(
                    "Cidade",
                    font_family="Seagon Medium",
                    color="white",
                    size=38,
                    weight=ft.FontWeight.BOLD
               )
          ],
     )

     central_container_row_2 = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          controls=[
               ft.Image(
                    src="http://openweathermap.org/img/wn/02d.png",
                    width=50,
                    height=50
               )
          ],
     )

     central_container_row_3 = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          controls=[
               ft.Text(
                    "38°",
                    font_family="Seagon Medium",
                    color="white",
                    size=28,
               )
          ],
     )

     central_container_row_4 = ft.Row(
          alignment=ft.MainAxisAlignment.CENTER,
          controls=[
               ft.Text(
                    "75%",
                    font_family="Seagon Medium",
                    color="white",
               )
          ],
     )



     main_container.content.controls.append(top_container)
     main_container.content.controls.append(central_container)
     top_container.content.controls.append(local_search)
     top_container.content.controls.append(btn_search)
     central_container.content.controls.append(central_container_row_1)
     central_container.content.controls.append(central_container_row_2)
     central_container.content.controls.append(central_container_row_3)
     central_container.content.controls.append(central_container_row_4)

     page.add(main_container)

ft.app(target=main)