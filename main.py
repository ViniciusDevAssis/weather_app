import flet as ft
import service as sv
from datetime import datetime

def main(page: ft.Page):
     def update_weather(e):
          city, country = local_search.value.split(',')
          climate_data = sv.get_weather_by_city(sv.api_key, city, country)
          
          central_container_row_1.controls[0].value = climate_data['name']
          central_container_row_2.controls[0].src = f"http://openweathermap.org/img/wn/{climate_data['weather'][0]['icon']}.png"
          central_container_row_3.controls[0].value = f"{int(climate_data['main']['temp'])}°C"
          central_container_row_4.controls[0].value = f"{climate_data['main']['humidity']}%"

          update_forecast()
          page.update()

     def update_forecast():
          city, country = local_search.value.split(',')
          forecast_data = sv.get_weather_forecast_by_city(sv.api_key, city, country)

          daily_forecast = []
          for item in forecast_data['list']:
               if '12:00:00' in item['dt_txt']:
                  daily_forecast.append(item)
               if len(daily_forecast) == 5:
                   break
               
          for i in range(5):
               date = daily_forecast[i]['dt_txt'].split()[0]
               date_obj = datetime.strptime(date, "%Y-%m-%d")
               icon = daily_forecast[i]['weather'][0]['icon']
               temp = int(daily_forecast[i]['main']['temp'])

               lower_container_row_1.controls[i].value = date_obj.strftime("%a")
               lower_container_row_2.controls[i].src = f"http://openweathermap.org/img/wn/{icon}.png"
               lower_container_row_3.controls[i].value = f"{temp}°C"

     page.update()

     
     
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
          expand=True,
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
          icon="Search",
          on_click=update_weather
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

     lower_container = ft.Container(
          expand=True,
          height=page.window.height * 0.2,
          content=ft.Column(

          )
     )

     lower_container_row_1 = ft.Row(
          alignment=ft.MainAxisAlignment.SPACE_AROUND,
          controls=[
               ft.Text(
                    f"D{i}",
                    color="white"
               )for i in range(1,6)
          ],
     )

     lower_container_row_2 = ft.Row(
          alignment=ft.MainAxisAlignment.SPACE_AROUND,
          controls=[
               ft.Image(
                    src=f"http://openweathermap.org/img/wn/0{i}d.png",
                    width=50,
                    height=50
               )for i in range(1,6)
          ],
     )

     lower_container_row_3 = ft.Row(
          alignment=ft.MainAxisAlignment.SPACE_AROUND,
          controls=[
               ft.Text(
                    f"T{i}",
                    color="white"
               )for i in range(1,6)
          ],
     )

     main_container.content.controls.append(top_container)
     main_container.content.controls.append(central_container)
     main_container.content.controls.append(lower_container)
     top_container.content.controls.append(local_search)
     top_container.content.controls.append(btn_search)
     central_container.content.controls.append(central_container_row_1)
     central_container.content.controls.append(central_container_row_2)
     central_container.content.controls.append(central_container_row_3)
     central_container.content.controls.append(central_container_row_4)
     lower_container.content.controls.append(lower_container_row_1)
     lower_container.content.controls.append(lower_container_row_2)
     lower_container.content.controls.append(lower_container_row_3)

     page.add(main_container)

ft.app(target=main)