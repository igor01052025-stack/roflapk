from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Цвет фона (можно сделать черным или красным)
Window.clearcolor = (0.05, 0.05, 0.05, 1)

class RoflApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.label = Label(
            text='⚠️ Внимание!\nОбнаружен опасный вирус!',
            font_size=22,
            halign='center',
            color=(1, 0, 0, 1)
        )
        
        btn = Button(
            text='Очистить телефон',
            size_hint=(1, 0.25),
            background_color=(0, 0.7, 1, 1)
        )
        btn.bind(on_press=self.on_button_click)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        self.label.text = 'Попался! 🤡\nТвои данные теперь у меня!'
        self.label.color = (0, 1, 0, 1)

if __name__ == '__main__':
    RoflApp().run()