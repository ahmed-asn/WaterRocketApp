import kivy
from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

import math
import pickle

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

class RocketLocationFenster(Screen, FloatLayout):
    pass

class RaketenGleichungFenster(Screen, FloatLayout):

    def rechne(self):
        startgewicht = float(self.ids["startgewicht"].text)
        leergewicht = float(self.ids["leergewicht"].text)
        startdruck = float(self.ids["startdruck"].text)
        austrittsradius = float(self.ids["austrittsradius"].text)
        austrittsquerschnitt = ((austrittsradius/2)**2) * math.pi

        wasser_volumen = (startgewicht-leergewicht)/1000
        dichte = 1000
        g = 9.81

        austrittsgeschw = round(math.sqrt((2*startdruck/dichte)),3)
        max_geschw = round(austrittsgeschw * math.log(startgewicht/leergewicht) - g *((startgewicht-leergewicht)/(dichte*austrittsquerschnitt*austrittsgeschw)),3)
        weg_1 = round(0.5 * max_geschw *(wasser_volumen/(austrittsquerschnitt*austrittsgeschw)),3)
        weg_2 = round((max_geschw**2)/(2*g),3)
        max_hoehe = round(weg_1 + weg_2, 3)

        ergebnisse = [austrittsgeschw, max_geschw, max_hoehe]
        with open("raketengleichungen_ergebnisse.txt", "wb") as datei:
            pickle.dump(ergebnisse, datei)


        print(max_geschw)
        print(austrittsgeschw)
        print(weg_1, weg_2, max_hoehe)

class RaketenGleichungRechnerFenster(Screen, FloatLayout):
    ergebnisse = []
    def on_enter(self, *args):

        with open("raketengleichungen_ergebnisse.txt", "rb") as datei:
            self.ergebnisse = pickle.load(datei)

        austrittsgeschw = "v_wasser = "+str(self.ergebnisse[0])
        max_geschw = "v_rakete = "+str(self.ergebnisse[1])
        max_hoehe = "h_max = "+str(self.ergebnisse[2])

        self.ids["austrittsgeschw"].text = austrittsgeschw
        self.ids["max_geschw"].text = max_geschw
        self.ids["max_hoehe"].text = max_hoehe




class FallschirmGleichungFenster(Screen, FloatLayout):

    def rechne(self):
        masse = float(self.ids["masse"].text)
        fallgeschw = float(self.ids["fallgeschw"].text)

        #konstanten
        g = 9.81
        C = 1.33
        p = 1.12

        flaeche = round((2*masse*g)/(C*p*(fallgeschw**2)), 3) * 10000
        laenge = round(math.sqrt((2*flaeche)/math.sqrt(27)), 3)


        ergebnisse = [flaeche, laenge]
        with open("fallschirmgleichungen_ergebnisse.txt", "wb") as datei:
            pickle.dump(ergebnisse, datei)


class FallschirmGleichungRechnerFenster(Screen, FloatLayout):
    ergebnisse = []

    def on_enter(self, *args):
        with open("fallschirmgleichungen_ergebnisse.txt", "rb") as datei:
            self.ergebnisse = pickle.load(datei)

        self.ids["flaeche"].text = "A = "+str(self.ergebnisse[0])
        self.ids["laenge"].text = "a = "+str(self.ergebnisse[1])



class WaterRocketApp(App):
    def build(self):
        return Builder.load_file("waterrocket_app.kv")


if __name__ == '__main__':
    WaterRocketApp().run()
