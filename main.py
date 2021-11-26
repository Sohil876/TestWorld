#!/usr/bin/python3
# TestWorld

# Minimum required kivy version
from kivy import require as Krequire
Krequire('2.0.0')

# Imports
from kivy.app import App
from kivy.uix.widget import Widget


class HelloWorld(Widget):
    pass


class MyApp(App):
    def build(self):
        return HelloWorld()


if __name__ == '__main__':
    MyApp().run()
