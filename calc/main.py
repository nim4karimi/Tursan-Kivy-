from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
<Calc>:
    # This are attributes of the class Calc now
    a: _a
    b: _b
    result: _result
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'screen1'
                GridLayout:
                    cols:1
                    TextInput:
                        id: _a
                        text: '3'
                    TextInput:
                        id: _b
                        text: '5'
                    Label:
                        id: _result
                    Button:
                        text: 'sum'
                        # You can do the opertion directly
                        on_press: _result.text = str(int(_a.text) + int(_b.text))
                    Button:
                        text: 'product'
                        # Or you can call a method from the root class (instance of calc)
                        on_press: root.product(*args)
            Screen:
                name: 'screen2'
                Label: 
                    text: 'The second screen'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, .1
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Go to Screen 2'
                on_press: _screen_manager.current = 'screen2'""")

class Calc(FloatLayout):
    # define the multiplication of a function
    def product(self, instance):
        # self.result, self.a and self.b where defined explicitely in the kv
        self.result.text = str(int(self.a.text) * int(self.b.text))

class TestApp(App):
    def build(self):
        return Calc()

if __name__ == '__main__':
    TestApp().run()