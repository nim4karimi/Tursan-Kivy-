

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard


# from kivy.uix.image import Image


# Config.set('kivy', 'keyboard_mode', 'systemandmulti')



class root(BoxLayout):

    def __init__(self, **kwargs):
        super(root, self).__init__(**kwargs)
        self.request_key

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
                diff = float(str(x-int(x))[:4])
                if diff !=0 and diff <= 0.5:
                    x = int(x) + 0.5
                else:
                    x = round(x)
                return x

            metrz = (float(self.arz.text) / 100) * (float(self.ertefa.text) / 100)
            roundMetr = NRound(metrz)

            if roundMetr < 1 :
                self.metr.text = str("1")
            else:
                self.metr.text = str(roundMetr)




            # -- Nakh 1 va 2
            self.nakha.text = str(((int(self.ertefa.text) + int(self.arz.text) ) *2 ) +30 )


            # -- Nakh 3
            nakhbb = int(self.ertefa.text)

            if nakhbb >= 170 :
                self.nakhb.text = str( ((float(self.ertefa.text) / 4 )*3) + (int(self.arz.text) * 2) +30)
            else:
                self.nakhb.text = str("--")


            if self.gheymat.text == '' :
                self.gheymat.text = str(int(1))
                self.gheymatKoll.text = ''
            else:
            # -- Gheyamt Koll
                self.gheymatKoll.text = str(float(roundMetr) * float(self.gheymat.text))

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



    def cleanz(self,instance):

        # - inputs
        self.ertefa.text = ''
        self.arz.text= ''
        self.gheymat.text=''


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


class HeroApp(App):
    kv_directory = 'template1'

    def build(self):
        return root()




if __name__ in ('__main__', '__android__'):
    HeroApp().run()
