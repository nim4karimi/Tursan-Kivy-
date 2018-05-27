import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label


class TursanApp(App):

    def build(self):
        return Label()

tursan = TursanApp()

tursan.run()