import flet as ft

def main(page: ft.Page):
    page.title = "Solex Modern Scientific Calculator"
    # Qindaa'ina Web irratti akka hin dhabbanneef
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 350
    page.window_height = 600
    
    result = ft.TextField(
        value="0", 
        text_align=ft.TextAlign.RIGHT, 
        width=300, 
        text_size=40, 
        color=ft.colors.WHITE,
        read_only=True,
        border=ft.InputBorder.NONE
    )

    def button_clicked(e):
        data = e.control.text
        if data == "AC":
            result.value = "0"
        elif data == "back": # Mallattoo Xiyyaa/Back
            if len(result.value) > 1:
                result.value = result.value[:-1]
            else:
                result.value = "0"
        elif data == "=":
            try:
                # Tooftaa herregaa sirreeffame
                val = result.value.replace("×", "*").replace("÷", "/")
                res = eval(val)
                result.value = str(int(res) if res == int(res) else res)
            except:
                result.value = "Error"
        else:
            if result.value == "0":
                result.value = data
            else:
                result.value += data
        page.update()

    def calc_button(text, color=ft.colors.GREY_900, t_color=ft.colors.WHITE):
        return ft.ElevatedButton(
            text=text, bgcolor=color, color=t_color, expand=1, height=75,
            on_click=button_clicked,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
        )

    page.add(
        ft.Container(content=result, padding=20, alignment=ft.alignment.bottom_right),
        ft.Column([
            ft.Row([calc_button("AC", color=ft.colors.ORANGE_700), calc_button("back", color=ft.colors.RED_700), calc_button("÷", color=ft.colors.ORANGE_400)]),
            ft.Row([calc_button("7"), calc_button("8"), calc_button("9"), calc_button("×", color=ft.colors.ORANGE_400)]),
            ft.Row([calc_button("4"), calc_button("5"), calc_button("6"), calc_button("-", color=ft.colors.ORANGE_400)]),
            ft.Row([calc_button("1"), calc_button("2"), calc_button("3"), calc_button("+", color=ft.colors.ORANGE_400)]),
            ft.Row([calc_button("0"), calc_button("00"), calc_button("."), calc_button("=", color=ft.colors.GREEN_700)]),
        ])
    )

# SARARA MURTEESSAA: GitHub Pages irratti akka hojjetuuf
if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
