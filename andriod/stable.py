from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard
from kivy.properties import ObjectProperty , NumericProperty
from kivy.uix.button import Button
from functools import partial
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy import require

require("1.0.7")


Builder.load_string('''

<ImageButton@Button>:
    source: None
    Image:
        source: root.source
        center: root.center
        allow_stretch : True
        
        
<IntroScreen>:
    BoxLayout:
        orientation:'vertical'
        canvas:
            Color :
                rgb : 1,1,1
            Rectangle:
                pos: self.pos
                size : self.size
        
        Image:
            source : 'img1.png'
        
        Button:
            text: "Vorod Be barname"
            size_hint_y: 0.1
            on_release: root.manager.current = "calc"
        

            

<CalcScreen>:
    ertefa : _ertefa
    arz : _arz
    gheymat : _gheymat

    ertefaFrame : _ertefaFrame
    arzFrame : _arzFrame
    motaharek : _motaharek

    ertefaTur : _ertefaTur
    gamTur : _gamTur
    metr : _metr


    nakha : _nakha
    nakhb : _nakhb


    gheymatKoll : _gheymatKoll


    BoxLayout:
        orientation:'vertical'
        canvas:
            Color :
                rgb : 1,1,1
            Rectangle:
                pos: self.pos
                size : self.size


    # -------------------------------------------
        GridLayout:
            rows:3
            col:2
            size_hint: 1, .4
            padding : 5


    # INPUT ---[ ERTEFA ASLI ]---------------------------

            TextInput:
                id: _ertefa
                input_filter : 'float'
                input_type : 'number'
                multiline: False
                font_size : '30sp'
                text: ''

            Image:
                source:'img1.png'

    # INPUT ---[ ARZ ASLI ]------------------------------

            TextInput:
                id: _arz
                input_filter : 'float'
                input_type : 'number'
                multiline: False
                font_size : '30sp'
                text: ''
            Image:
                source:'img2.png'

    # INPUT ---[ GHEYMAT ]--------------------------------

            TextInput:
                id: _gheymat
                input_filter : 'float'
                input_type : 'number'
                multiline: False
                font_size : '30sp'
                text: ''
            Image:
                source:'img3.png'



    # ----------------------------------------------------
        GridLayout:
            id: 'outputs'
            rows:11
            col:2
            padding : 5


    # OUTPUT ---[ ERTEFA FRAME ]--------------------------

            # PROC --[ Def Button ]------------------------------



            ImageButton :
                source : 'calc.png'
                # text: 'Mohasebe'
                on_press : root.product(*args)
                # background_down : 'btt.jpg'
                background_normal : 'btn1.png'

            ImageButton :
                source : 'dele.png'
                background_down : 'btn2.png'
                on_press : root.cleanz(*args)


            Label:
                id : _ertefaFrame
                text: ''
                color : 0,0,0,1
                bold : True


            Image:
                source:'out1.png'


    # OUTPUT ---[ ARZ FRAME ]--------------------------

            Label:
                id : _arzFrame
                text: ''
                color : 0,0,0,1
                bold : True

            Image:
                source:'out2.png'


    # OUTPUT ---[ MOTAHAREK ]--------------------------
            Label:
                id : _motaharek
                text: ''
                color : 0,0,0,1


            Image:
                source:'out3.png'


    # OUTPUT ---[ ERTEFA TUR ]------------------------
            Label:
                id : _ertefaTur
                text: ''
                color : 0,0,0,1
            Image:
                source:'out4.png'


    # OUTPUT ---[ GAM TUR ]---------------------------

            Label:
                id : _gamTur
                text: ''
                color : 0,0,0,1

            Image:
                source:'out5.png'

    # OUTPUT ---[ Nakh 1 va 2 ]---------------------------

            Label:
                id : _nakha
                text: ''
                color : 0,0,0,1

            Image:
                source:'outnakh.png'

    # OUTPUT ---[ Nakh 3 ]---------------------------

            Label:
                id : _nakhb
                text: ''
                color : 0,0,0,1

            Image:
                source:'outnakh2.png'

    # OUTPUT ---[ METRE MORABA ]------------------------
            Label:
                id : _metr
                text: ''
                color : 0,0,0,1

            Image:
                source:'out6.png'

    # OUTPUT ---[ GHEYMAT KOLL ]------------------------
            Label:
                id: _gheymatKoll
                text: ''
                bold: True
                color : 1,0,0,1
                font_size : '30sp'

            Image:
                source:'out7.png'

    # INFO ---[ ADDRESS ]------------------------
        Image:
            source:'down.png'
            size_hint: 1, None    

''')

class IntroScreen(Screen):
    pass

class CalcScreen(Screen):



    def __init__(self, **kwargs):
        super(CalcScreen, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            vkeyboard = self._keyboard.widget
            vkeyboard.layout = 'numeric.json'

        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True


    # -- For define
    def product(self, instance):
        try:
            # -- Ertefa Frame
            self.ertefaFrame.text = str(int(self.ertefa.text) - 6)
            # -- Arze Frame
            self.arzFrame.text = str(int(self.arz.text) - 6)
            # -- Motahrek
            self.motaharek.text = str(float(self.ertefa.text) - 7.5)
            # -- Ertefa Tur
            self.ertefaTur.text = str(float(self.ertefa.text) - 3.5)
            # -- Game Tur
            self.gamTur.text = str(float(self.arz.text) / 2.5)

            # -- Metre morab

            def NRound(x):
                diff = float(str(x - int(x))[:4])
                if diff != 0 and diff <= 0.5:
                    x = int(x) + 0.5
                else:
                    x = round(x)
                return x

            metrz = (float(self.arz.text) / 100) * (float(self.ertefa.text) / 100)
            roundMetr = NRound(metrz)

            if roundMetr < 1:
                self.metr.text = str("1")
                gg = self.metr.text
            else:
                self.metr.text = str(roundMetr)
                gg = self.metr.text

            # -- Nakh 1 va 2
            self.nakha.text = str(((int(self.ertefa.text) + int(self.arz.text)) * 2) + 30)

            # -- Nakh 3
            nakhbb = int(self.ertefa.text)

            if nakhbb >= 170:
                self.nakhb.text = str(((float(self.ertefa.text) / 4) * 3) + (int(self.arz.text) * 2) + 30)
            else:
                self.nakhb.text = str("--")

            if self.gheymat.text == '':
                self.gheymat.text = str(int(1))
                self.gheymatKoll.text = ''
            else:
                # -- Gheyamt Koll
                self.gheymatKoll.text = str(float(gg) * float(self.gheymat.text))

        except Exception:
            self.ertefa.text = ''
            self.arz.text = ''
            self.gheymat.text = ''

            # -- Ertefa Frame
            self.ertefaFrame.text = ''
            # -- Arze Frame
            self.arzFrame.text = ''
            # -- Motahrek
            self.motaharek.text = ''
            # -- Ertefa Tur
            self.ertefaTur.text = ''
            # -- Game Tur
            self.gamTur.text = ''
            # -- Metre morab
            self.metr.text = ''
            # -- Gheyamt Koll
            self.gheymatKoll.text = ''

            self.nakha.text = ''
            self.nakhb.text = ''

    def cleanz(self, instance):

        # - inputs
        self.ertefa.text = ''
        self.arz.text = ''
        self.gheymat.text = ''

        # -- Ertefa Frame
        self.ertefaFrame.text = ''
        # -- Arze Frame
        self.arzFrame.text = ''
        # -- Motahrek
        self.motaharek.text = ''
        # -- Ertefa Tur
        self.ertefaTur.text = ''
        # -- Game Tur
        self.gamTur.text = ''
        # -- Metre morab
        self.metr.text = ''
        # -- Gheyamt Koll
        self.gheymatKoll.text = ''

        self.nakha.text = ''
        self.nakhb.text = ''


class TursanApp(App):
    sm = None # The root Screen manager

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(IntroScreen(name="intro"))
        self.sm.add_widget(CalcScreen(name='calc'))
        self.sm.current = 'intro'
        return self.sm

if __name__ in ('__main__', '__android__'):
    Tursan = TursanApp()
    Tursan.run()