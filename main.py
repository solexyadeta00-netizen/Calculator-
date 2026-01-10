import flet as ft

def main(page: ft.Page):
    # Qindaa'ina Fuulaa (Page Settings)
    page.title = "Solex Modern Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    page.window_width = 380
    page.window_height = 650
    page.padding = 20
    
    # Ibsituu (Display)
    result = ft.Text(
        value="0", 
        color=ft.colors.WHITE, 
        size=50, 
        weight=ft.FontWeight.W_300
    )

    def button_clicked(e):
        data = e.control.text
        
        if data == "AC":
            result.value = "0"
        elif data == "back":
            if len(result.value) > 1:
                result.value = result.value[:-1]
            else:
                result.value = "0"
        elif data == "=":
            try:
                # Tooftaa herregaa
                expression = result.value.replace("×", "*").replace("÷", "/")
                res = eval(expression)
                # Yoo lakkoofsi bu'aa .0 qabaate balleessuu
                result.value = str(int(res) if res == int(res) else round(res, 4))
            except:
                result.value = "Error"
        else:
            if result.value == "0":
                result.value = data
            else:
                result.value += data
        page.update()

    # Akkaataa Kiyyuubotaa (Modern Button Design)
    def calc_button(text, color="#1C1C1E", t_color=ft.colors.WHITE):
        return ft.Container(
            content=ft.Text(text, size=24, color=t_color),
            alignment=ft.alignment.center,
            width=75,
            height=75,
            bgcolor=color,
            border_radius=40,
            on_click=button_clicked,
            animate=ft.animation.Animation(300, ft.AnimationCurve.DECELERATE),
        )

    # UI Qindeessuu
    page.add(
        ft.Column(
            controls=[
                # Display Area
                ft.Container(
                    content=result,
                    alignment=ft.alignment.bottom_right,
                    padding=ft.padding.only(right=20, top=100, bottom=40),
                ),
                # Buttons Grid
                ft.Column([
                    ft.Row([
                        calc_button("AC", color="#A5A5A5", t_color=ft.colors.BLACK),
                        calc_button("back", color="#A5A5A5", t_color=ft.colors.BLACK),
                        calc_button("÷", color="#FF9F0A"),
                    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    ft.Row([
                        calc_button("7"), calc_button("8"), calc_button("9"),
                        calc_button("×", color="#FF9F0A"),
                    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    ft.Row([
                        calc_button("4"), calc_button("5"), calc_button("6"),
                        calc_button("-", color="#FF9F0A"),
                    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    ft.Row([
                        calc_button("1"), calc_button("2"), calc_button("3"),
                        calc_button("+", color="#FF9F0A"),
                    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    ft.Row([
                        calc_button("0", color="#1C1C1E"), 
                        calc_button("00"), 
                        calc_button("."),
                        calc_button("=", color="#FF9F0A"),
                    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                ], spacing=15)
            ]
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
