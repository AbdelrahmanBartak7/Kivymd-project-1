from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.config import Config
Config.set('kivy', 'show_splash_screen', '0')  # تعطيل شاشة البداية

# يمكنك ضبط حجم النافذة لتناسب الآلة الحاسبة
Window.size = (350, 550)

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    md_bg_color: app.theme_cls.bg_dark

    MDLabel:
        id: display
        text: app.display_text
        font_size: 40
        halign: 'right'
        valign: 'bottom'
        size_hint_y: None
        height: 100
        theme_text_color: 'Custom'
        text_color: 1, 1, 1, 1
        bold: True
        padding: 10, 10

    MDGridLayout:
        cols: 4
        spacing: 10
        padding: 5
        size_hint_y: None
        height: self.minimum_height

        # الصف الأول
        MDRaisedButton:
            text: 'C'
            on_release: app.clear()
            md_bg_color: .9, .1, .1, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '('
            on_release: app.append_text('(')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: ')'
            on_release: app.append_text(')')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '/'
            on_release: app.append_text('/')
            md_bg_color: .9, .6, .1, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        # الصف الثاني
        MDRaisedButton:
            text: '7'
            on_release: app.append_text('7')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '8'
            on_release: app.append_text('8')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '9'
            on_release: app.append_text('9')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '*'
            on_release: app.append_text('*')
            md_bg_color: .9, .6, .1, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        # الصف الثالث
        MDRaisedButton:
            text: '4'
            on_release: app.append_text('4')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '5'
            on_release: app.append_text('5')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '6'
            on_release: app.append_text('6')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '-'
            on_release: app.append_text('-')
            md_bg_color: .9, .6, .1, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        # الصف الرابع
        MDRaisedButton:
            text: '1'
            on_release: app.append_text('1')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '2'
            on_release: app.append_text('2')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '3'
            on_release: app.append_text('3')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '+'
            on_release: app.append_text('+')
            md_bg_color: .9, .6, .1, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        # الصف الخامس
        MDRaisedButton:
            text: '0'
            on_release: app.append_text('0')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24


        MDRaisedButton:
            text: '.'
            on_release: app.append_text('.')
            md_bg_color: .2, .2, .2, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: 'D'
            on_release: app.backspace()
            md_bg_color: .5, .5, .5, 1
            text_color: 1, 1, 1, 1
            font_size: 24

        MDRaisedButton:
            text: '='
            on_release: app.calculate()
            md_bg_color: .1, .5, .8, 1
            text_color: 1, 1, 1, 1
            font_size: 24
'''


class CalculatorApp(MDApp):
    display_text = StringProperty('0')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def append_text(self, text):
        if self.display_text == '0' and text not in '+-*/':
            self.display_text = text
        else:
            self.display_text += text

    def clear(self):
        self.display_text = '0'

    def backspace(self):
        if len(self.display_text) == 1:
            self.display_text = '0'
        else:
            self.display_text = self.display_text[:-1]

    def calculate(self):
        try:
            result = str(eval(self.display_text))
            self.display_text = result
        except Exception as e:
            self.display_text = 'Error'


if __name__ == '__main__':
    CalculatorApp().run()
