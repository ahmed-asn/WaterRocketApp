import kivy
from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder



class WindowManager(ScreenManager):
    pass


class HomeFenster(Screen, FloatLayout):
    pass


class AutoRechnerFenster(Screen, FloatLayout):
    pass

class AutoRechnungenFenster(Screen, FloatLayout):
    pass



class ManuellRechnerFenster(Screen, FloatLayout):
    pass

class ManuellRechnungenFenster(Screen, FloatLayout):
    pass


class PreRechnerFenster(Screen, FloatLayout):
    pass



class WaterRocketApp(App):
    def build(self):
        return Builder.load_file("waterrocket_app.kv")


if __name__ == '__main__':
    WaterRocketApp().run()