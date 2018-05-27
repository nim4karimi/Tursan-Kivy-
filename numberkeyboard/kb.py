from kivy.app import App
from kivy.uix.label import Label
from kivy.logger import Logger
from kivy.uix.vkeyboard import VKeyboard
from kivy import kivy_data_dir
import shutil
import os
from kivy.core.window import Window


class KeyboardListener():
    ''' The class that binds to and obtains then keyboard classback '''
    def __init__(self):
        ''' Ensure that our keyboard definition is in the correct folder '''
        destPath = os.path.join(kivy_data_dir, "keyboards", "numeric.json")
        if not os.path.exists(destPath):
            try:
                shutil.copy(os.path.abspath("./numeric.json"), destPath)
                Logger.info("keyboard.py: copied keyboard to " + destPath)
            except Exception as e:
                Logger.info("keyboard.py: Error copying keyboard " + str(e))
        else:
            Logger.info("keyboard.py: keyboard in " + destPath)

    def setCallback(self, callback):
        ''' Set the function to be called when key presses occur '''
        Logger.info("Keyboard.py: Binding to " + str(callback))
        VKeyboard.layout = "numeric"
        self._keyboard = Window.request_keyboard(
            self._keyboard_close,
            self)
        # For setting keyboard - never shows 'numeric' keyboard?
        self._keyboard.layout = "numeric"
        VKeyboard.layout = "numeric"
        #vk = VKeyboard()
        #vk.layout = kwargs["layout"]
        #self._keyboard.widget = vk
        #vk.refresh()
        #Window.set_vkeyboard_class(vk)
        self._keyboard.bind(on_key_down=callback)
        self.callback = callback

    def _keyboard_close(self):
        ''' The keyboard has been closed '''
        if self.callback:
            Logger.info("Keyboard.py: Unbinding from " + str(self.callback))
            self._keyboard.unbind(on_key_down=self.callback)
            self._keyboard = None
            self.callback = None


class TestWidget(Label):
    ''' A Stub windget'''


class KeyboardTestApp(App):
    def build(self):
        self.label = TestWidget(text="Hello")
        KeyboardListener().setCallback(self.key_down)
        return self.label

    def key_down(self, keyboard, keycode, text, modifiers):
        self.label.text = self.label.text + keycode[1]

if  __name__ == '__main__':
    KeyboardTestApp().run()