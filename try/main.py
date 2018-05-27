import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App

import arabic_reshaper
from bidi.algorithm import get_display


ertefa_text = arabic_reshaper.reshape(u'ارتفاع اصلی')
reshape_ertefa_text = get_display(ertefa_text)


Builder.load_string('''
<HelloWorldScreen>:
    cols: 2
    Label:
        text: {0}
    Button:
        text: 'Click me! %d' % root.counter
        on_release: root.my_callback()
''')

class HelloWorldScreen(GridLayout):
    counter = NumericProperty(0)
    def my_callback(self):
        # print 'The button has been pushed'
        self.counter += 1

class HelloWorldApp(App):
    def build(self):
        self.icon = 'icon.png'
        return HelloWorldScreen()

if __name__ == '__main__':
    HelloWorldApp().run()