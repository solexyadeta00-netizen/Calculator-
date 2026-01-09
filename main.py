import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Iskiriinii mobile fakkeessuuf (Pydroid irratti barbaachisaa miti)
Window.clearcolor = (0.05, 0.05, 0.05, 1)

class ScientificCalc(App):
    def build(self):
        self.operators = ["/", "*", "+", "-", "^"]
        self.main_layout = BoxLayout(orientation="vertical", padding=15, spacing=10)
        
        # Ibsituu Bu'aa (Display) - Modern Look
        self.display = TextInput(
            multiline=False, readonly=True, halign="right",
            font_size=60, background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1), size_hint=(1, 0.3),
            padding=[10, 20, 10, 20], cursor_color=(0, 1, 0, 1)
        )
        self.main_layout.add_widget(self.display)
        
        # Furtuulee (Buttons) - Grid System
        button_grid = GridLayout(cols=4, spacing=10, size_hint=(1, 0.7))
        
        # Mallattoolee furtuulee
        buttons = [
            'sin', 'cos', 'tan', 'sqrt',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
            '(', ')', '^', '='
        ]
        
        for btn_text in buttons:
            # Halluu furtuulee gargar baasuu
            if btn_text in ['sin', 'cos', 'tan', 'sqrt', '^', '(', ')']:
                bg_color = (0.2, 0.2, 0.25, 1) # Scientific (Dull Blue)
            elif btn_text in ['/', '*', '-', '+', '=']:
                bg_color = (0.9, 0.5, 0, 1)    # Operators (Orange)
            elif btn_text == 'C':
                bg_color = (0.7, 0.1, 0.1, 1)  # Clear (Red)
            else:
                bg_color = (0.15, 0.15, 0.15, 1) # Numbers (Dark Grey)

            button = Button(
                text=btn_text, background_normal='',
                background_color=bg_color, font_size=24,
                bold=True
            )
            
            if btn_text == '=':
                button.bind(on_press=self.on_solution)
            elif btn_text == 'C':
                button.bind(on_press=self.clear_display)
            else:
                button.bind(on_press=self.on_button_click)
                
            button_grid.add_widget(button)
            
        self.main_layout.add_widget(button_grid)
        return self.main_layout

    def on_button_click(self, instance):
        current = self.display.text
        button_text = instance.text
        
        # Funksinoonni saayinsii akka banaman gochuu
        if button_text in ['sin', 'cos', 'tan', 'sqrt']:
            self.display.text += button_text + "("
        else:
            self.display.text += button_text

    def clear_display(self, instance):
        self.display.text = ""

    def on_solution(self, instance):
        text = self.display.text
        try:
            # Python 'math' library fayyadamnee herregguuf
            # Kufaatii hambisuuf 'sin' kkf replace goona
            expr = text.replace('sin', 'math.sin(math.radians')
            expr = expr.replace('cos', 'math.cos(math.radians')
            expr = expr.replace('tan', 'math.tan(math.radians')
            expr = expr.replace('sqrt', 'math.sqrt')
            expr = expr.replace('^', '**')
            
            # Hir'ina qolloo (brackets) guutuu
            open_count = expr.count('(')
            close_count = expr.count(')')
            if open_count > close_count:
                expr += ')' * (open_count - close_count)
            
            self.display.text = str(round(eval(expr), 8))
        except Exception:
            self.display.text = "Error"

if __name__ == "__main__":
    ScientificCalc().run()
    ft.app(target=main)
